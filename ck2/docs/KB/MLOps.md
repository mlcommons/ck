# KB: MLOps and MLPerf

One of our goals is to automate the development, optimization and deployment of Pareto-efficient ML Systems in production. 
The main challenge is how to support numerous and continuously changing software and hardware. 
Here we collect related notes about MLPerf, MLOps, DevOps, inference engines, containers and production deployment of ML systems.

# News and articles

- March 2022: [MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess)
- Jun 2022: [Making ML models more portable and reproducible with open APIs, reusable best practices and MLOps](https://arxiv.org/abs/2006.07161)


# MLPerf inference benchmark

- [MLCommons website](https://mlcommons.org)

# Inference engines

- [Nvidia Triton inference server](https://developer.nvidia.com/nvidia-triton-inference-server)

# Deployment platforms

- [Seldon Deploy](https://www.seldon.io/solutions/deploy)
  - [About](https://deploy.seldon.io/en/v1.4/contents/about/index.html)
  - [Architecture](https://deploy.seldon.io/en/v1.4/contents/architecture/index.html)
- AWS
- Azure

# ML workflow and automation frameworks

- [MLFlow](https://mlflow.org/)
- [Kubeflow](https://www.kubeflow.org)
- [AWS SageMaker](https://aws.amazon.com/pm/sagemaker)
- [Kedro](https://github.com/kedro-org/kedro)
- [Redun: "yet another redundant workflow engine"]( https://github.com/insitro/redun )
- [Collective Knowledge](https://github.com/mlcommons/ck)


# ML exchange formats

- [ONNX](https://onnx.ai)
- [NNEF (Khronos)](https://www.khronos.org/nnef)

# Containers

- Docker
- Kubernetes
- Singularity
- Misc:
    - [Containerizing Huggingface Transformers for GPU inference with Docker and FastAPI on AWS](https://towardsdatascience.com/containerizing-huggingface-transformers-for-gpu-inference-with-docker-and-fastapi-on-aws-d4a83edede2f) (TowardsDataScience, 20211004)
    - [FOSDEM’22 containers track](https://fosdem.org/2022/schedule/track/containers/)

