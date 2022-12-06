import abc
import contextlib
import logging
import typing

import mlperf_loadgen

from loadgen.model import ModelInput, ModelInputSampler

logger = logging.getLogger(__name__)


QueryInput = typing.Dict[int, ModelInput]
QueryResult = typing.Dict[int, typing.Any]


class ModelRunner(contextlib.AbstractContextManager):
    @abc.abstractmethod
    def issue_query(self, query: QueryInput) -> typing.Optional[QueryResult]:
        pass

    # Optional method to flush pending queries
    def flush_queries(self) -> typing.Optional[QueryResult]:
        pass

    def __exit__(self, _exc_type, _exc_value, _traceback):
        logger.info(f"{self} : Exited")
        return None


class Harness:
    def __init__(self, sampler: ModelInputSampler, runner: ModelRunner):
        self.sampler = sampler
        self.runner = runner
        self.samples = None

    def load_query_samples(self, query_samples):
        assert self.samples is None
        self.samples = dict()
        for query_id in query_samples:
            self.samples[query_id] = self.sampler.sample(query_id)
        logger.info(f"Loaded {len(self.samples)} samples")

    def unload_query_samples(self, _query_samples):
        assert self.samples is not None
        logger.info(f"Unloaded samples")
        self.samples = None

    def issue_query(self, query_samples):
        query_input = dict()
        for q in query_samples:
            # logger.info(f"Query Id: {q.id}, SampleIndex: {q.index}")
            input = self.samples[q.index]
            query_input[q.id] = input
        result = self.runner.issue_query(query_input)
        logger.info(f"Queries issued {len(query_input)}")
        if result is not None:
            self._complete_query(result)

    # Called after the last call to issue queries in a series is made.
    # Client can use this to flush any deferred queries rather than waiting for a timeout.
    def flush_queries(self):
        result = self.runner.flush_queries()
        logger.info(f"Queries flushed")
        if result is not None:
            self._complete_query(result)

    def _complete_query(self, result: QueryResult):
        responses = []
        for query_id, _query_result in result.items():
            response_data, response_size = 0, 0
            response = mlperf_loadgen.QuerySampleResponse(
                query_id, response_data, response_size
            )
            responses.append(response)
        mlperf_loadgen.QuerySamplesComplete(responses)
