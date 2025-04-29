import array
import json
import logging
import queue
import sys
import threading
import time

import mlperf_loadgen as lg
import numpy as np
import requests
import torch
from dataset import Dataset
from transformers import AutoTokenizer
from transformers.generation.streamers import BaseStreamer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("DeepSeek-R1")

gen_kwargs = {
    "early_stopping": True,
    "max_new_tokens": 1024,
    "min_new_tokens": 1,
    "num_beams": 1,
    "do_sample": False,
}


class FirstTokenStreamer(BaseStreamer):
    """Streams first tokens to a 'holder'"""

    def __init__(
        self, first_token, tokens_cache=None, is_first_token=True, response_ids=None
    ):
        """Response ids added to 'sign' the first token"""

        self.first_token = first_token
        self.is_first_token = is_first_token
        self.tokens_cache = tokens_cache or []
        self.response_ids = response_ids or []
        self.is_prompt = True

    def put(self, value):
        """Caches the tokens as they're generated. Assumes bs=1"""

        if self.is_prompt:
            self.is_prompt = False
            return

        value = value.item()
        if self.is_first_token:
            self.first_token.put((value, self.response_ids[0]))
            self.is_first_token = False
            return

        self.tokens_cache.append(value)

    def end(self):
        pass

    def get_out_tokens(self):
        return self.tokens_cache


class SUT:
    def __init__(
        self,
        model_path,
        api_server=None,
        device="cpu",
        batch_size=32,
        total_sample_count=24576,
        dataset_path=None,
        use_cached_outputs=False,
        workers=1,
    ):

        self.model_path = model_path
        self.device = device
        self.api_servers = []
        if api_server:
            self.api_servers.append(api_server)

        self.batch_size = batch_size

        if "cuda" in self.device:
            assert torch.cuda.is_available(), "torch gpu is not available, exiting..."

        self.dataset_path = dataset_path
        self.data_object = Dataset(
            self.model_path,
            total_sample_count=total_sample_count,
            dataset_path=self.dataset_path,
            device=self.device,
        )
        self.qsl = lg.ConstructQSL(
            self.data_object.total_sample_count,
            self.data_object.perf_count,
            self.data_object.LoadSamplesToRam,
            self.data_object.UnloadSamplesFromRam,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path,
            model_max_length=1024,
            padding_side="left",
            use_fast=True,
        )

        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.num_workers = workers
        self.worker_threads = [None] * self.num_workers
        self.query_queue = queue.Queue()

        self.use_cached_outputs = use_cached_outputs
        self.sample_counter = 0
        self.sample_counter_lock = threading.Lock()
        self.remaining_samples = total_sample_count

    def start(self):
        for j in range(self.num_workers):
            worker = threading.Thread(target=self.process_queries)
            worker.start()
            self.worker_threads[j] = worker

    def stop(self):
        for _ in range(self.num_workers):
            self.query_queue.put(None)

        for worker in self.worker_threads:
            worker.join()

    def query_api_vllm(self, inputs, idx):
        headers = {"Content-Type": "application/json"}
        json_data = {
            "model": self.model_path,
            "prompt": inputs,
            "min_tokens": 1,
            "max_tokens": 1024,
        }

        response_code = 0
        print(f"Server path {self.api_servers[idx]}/v1/completions")
        while response_code != 200:
            try:
                response = requests.post(
                    url=f"{self.api_servers[idx]}/v1/completions",
                    headers=headers,
                    json=json_data,
                    verify=False,
                )
                response_code = response.status_code
            except Exception as e:
                print(e)
                print("connection failure")
                break
        return [resp["text"] for resp in json.loads(response.text)["choices"]]

    def api_action_handler(self, chunk, server_idx):
        output = self.query_api_vllm(chunk, server_idx)
        return output

    def process_queries(self):
        """Process batched queries from queue"""
        while True:
            batch = self.query_queue.get()
            if batch is None:
                break

            with self.sample_counter_lock:
                if self.sample_counter >= self.remaining_samples:
                    continue

                remaining = self.remaining_samples - self.sample_counter
                if len(batch) > remaining:
                    batch = batch[:remaining]

            input_ids_tensor = []
            for q in batch:
                input_ids_tensor.append(self.data_object.input_ids[q.index].tolist())

            tik = time.time()

            decoded = self.tokenizer.batch_decode(input_ids_tensor)
            cleaned = [
                entry.replace("</s>", "").replace("<s>", "") for entry in decoded
            ]

            if self.api_servers:
                output = self.api_action_handler(cleaned, 0)
            else:
                print("Error: No API server specified")
                exit(1)

            processed_output = self.tokenizer(output)["input_ids"]
            for i, q in enumerate(batch):
                unpadded = np.array(processed_output[i])
                n_tokens = unpadded.shape[0]
                response_array = array.array("B", unpadded.tobytes())
                bi = response_array.buffer_info()
                response = [lg.QuerySampleResponse(q.id, bi[0], bi[1], n_tokens)]
                lg.QuerySamplesComplete(response)

            tok = time.time()

            with self.sample_counter_lock:
                self.sample_counter += len(batch)
                if self.sample_counter >= self.remaining_samples:
                    self.stop()
                print(
                    f"Processed batch of {len(batch)}, "
                    f"total samples: {self.sample_counter}/{self.remaining_samples}"
                )
                print(f"\tBatch processing time: {tok - tik:.2f}s")

    def get_sut(self):
        self.sut = lg.ConstructSUT(self.issue_queries, self.flush_queries)
        return self.sut

    def get_qsl(self):
        return self.qsl

    def predict(self, **kwargs):
        raise NotImplementedError

    def issue_queries(self, query_samples):
        """Process queries in batches of batch_size"""
        print(
            f"Processing {len(query_samples)} samples in batches of {self.batch_size}"
        )
        print(f"Remaining samples to process: {self.remaining_samples}")

        query_samples = query_samples[: self.remaining_samples]

        for i in range(0, len(query_samples), self.batch_size):
            batch = query_samples[i : i + self.batch_size]
            self.query_queue.put(batch)

        print(f"Queued {len(query_samples)} samples in batches")

    def flush_queries(self):
        pass

    def __del__(self):
        pass


class SUTServer(SUT):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.first_token_queue = queue.Queue()

        with open(f"{self.model_path}/tokenizer.json", "r") as token_file:
            deepseek_tokenizer = json.load(token_file)
        self.deepseek_vocab = deepseek_tokenizer["model"]["vocab"]

    def start(self):

        for j in range(self.num_workers):
            worker = threading.Thread(target=self.process_queries)
            worker.start()
            self.worker_threads[j] = worker

        self.ft_response_thread = threading.Thread(target=self.process_first_tokens)
        self.ft_response_thread.start()

    def process_first_tokens(self):

        while True:
            first_token_item = self.first_token_queue.get()

            if first_token_item is None:
                log.info("Exiting First token response thread")
                break

            first_tokens, response_id = first_token_item

            response_data = array.array(
                "B", np.array(first_tokens, np.float32).tobytes()
            )
            bi = response_data.buffer_info()
            response = [lg.QuerySampleResponse(response_id, bi[0], bi[1])]
            lg.FirstTokenComplete(response)

    def stream_api_vllm(self, input, response_ids, idx):
        headers = {"Content-Type": "application/json"}
        json_data = {
            "model": self.model_path,
            "prompt": input,
            "max_tokens": 1024,
            "temperature": 0,
            "stream": True,
            "logprobs": 1,
        }

        while True:
            try:
                token_cache = []
                s = requests.Session()
                first = True
                with s.post(
                    f"{self.api_servers[idx]}/v1/completions",
                    headers=headers,
                    json=json_data,
                    verify=False,
                    stream=True,
                ) as resp:
                    for line in resp.iter_lines():
                        if line:
                            decoded = line.decode()
                            if decoded.startswith("data") and "[DONE]" not in decoded:
                                inter = json.loads(decoded[6:])["choices"][0][
                                    "logprobs"
                                ]
                                if "top_logprobs" in inter:
                                    token_s = list(inter["top_logprobs"][0].keys())[0]
                                    token = self.deepseek_vocab[token_s]
                                    if first:
                                        self.first_token_queue.put(
                                            (token, response_ids[0])
                                        )
                                        first = False
                                    token_cache.append(token)
                s.close()
                if token_cache:
                    return token_cache
            except Exception as e:
                s.close()
                print("Connection failure")
                print(f"An exception occurred: {type(e).__name__}")
                print(f"Exception details: {e}")

    def async_process_query(self, input_ids_tensor, qitem_id, idx):
        decoded = self.tokenizer.decode(input_ids_tensor[0])
        response_ids = [qitem_id]
        output_tokens = self.stream_api_vllm(decoded, response_ids, idx)
        n_tokens = len(output_tokens)
        if n_tokens <= 1:
            print("WARNING: caught low token count")
            print(input_ids_tensor)
            print(output_tokens)
        response_array = array.array("B", np.array(output_tokens, np.int32).tobytes())
        bi = response_array.buffer_info()
        response = [lg.QuerySampleResponse(qitem_id, bi[0], bi[1], n_tokens)]
        lg.QuerySamplesComplete(response)
        sys.exit()

    def process_queries(self):
        """Processor of the queued queries. User may choose to add batching logic"""
        server_idx = 0
        while True:

            qitem = self.query_queue.get()
            if qitem is None:
                break

            input_ids_tensor = self.data_object.input_ids[qitem.index]
            input_masks_tensor = self.data_object.attention_masks[qitem.index]

            if self.api_servers:
                threading.Thread(
                    target=self.async_process_query,
                    args=(input_ids_tensor, qitem.id, server_idx),
                ).start()
                server_idx = (server_idx + 1) % len(self.api_servers)
            else:
                tokens_cache = []
                tokens_streamer = FirstTokenStreamer(
                    self.first_token_queue,
                    tokens_cache=tokens_cache,
                    is_first_token=True,
                    response_ids=[qitem.id],
                )

                _ = self.model.generate(
                    input_ids=input_ids_tensor,
                    attention_mask=input_masks_tensor,
                    pad_token_id=self.tokenizer.pad_token_id,
                    streamer=tokens_streamer,
                    **gen_kwargs,
                )

                output_tokens = tokens_streamer.get_out_tokens()

                n_tokens = len(output_tokens)
                response_array = array.array(
                    "B", np.array(output_tokens, np.int32).tobytes()
                )
                bi = response_array.buffer_info()
                response = [lg.QuerySampleResponse(qitem.id, bi[0], bi[1], n_tokens)]
                lg.QuerySamplesComplete(response)

    def issue_queries(self, query_samples):
        """Process queries in batches like parent class"""
        print(
            f"Processing {len(query_samples)} samples in batches of {self.batch_size}"
        )

        for i in range(0, len(query_samples), self.batch_size):
            batch = query_samples[i : i + self.batch_size]
            self.query_queue.put(batch)

        print("Queued all samples in batches")

    def stop(self):
        for _ in range(self.num_workers):
            self.query_queue.put(None)

        for worker in self.worker_threads:
            worker.join()

        self.first_token_queue.put(None)
        self.ft_response_thread.join()
