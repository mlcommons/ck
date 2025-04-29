```sh
uv sync
source .venv/bin/activate
```

```sh
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
```

If the model is too big, you can add the `--tensor-parallel-size 8` argument.

```sh
python main.py \
    --scenario Offline \
    --accuracy \
    --total-sample-count 10 \
    --batch-size 2 \
    --device cuda:0 \
    --vllm \
    --api-server http://localhost:8000/
```

```sh
python accuracy_check.py --output-path accuracy_results.csv
```
