# KB: MLOps and MLPerf

One of our goals is to automate the development, optimization and deployment of Pareto-efficient ML Systems in production. 
The main challenge is how to support numerous and continuously changing software and hardware. 
Here we collect related notes about MLPerf, MLOps, DevOps, inference engines, containers and production deployment of ML systems.

# News and articles

- March 2022: [MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess)
- June 2022: [Making ML models more portable and reproducible with open APIs, reusable best practices and MLOps](https://arxiv.org/abs/2006.07161)


# MLPerf inference benchmark

- [MLCommons website](https://mlcommons.org)

# Inference engines

- [Nvidia Triton inference server](https://developer.nvidia.com/nvidia-triton-inference-server)

# Deployment platforms

- Azure
- AWS
- [Seldon Deploy](https://www.seldon.io/solutions/deploy)
  - [About](https://deploy.seldon.io/en/v1.4/contents/about/index.html)
  - [Architecture](https://deploy.seldon.io/en/v1.4/contents/architecture/index.html)

# ML platforms

- [HPE (press-release 2022-04-27)](https://www.hpe.com/us/en/newsroom/press-release/2022/04/hewlett-packard-enterprise-accelerates-ai-journey-from-poc-to-production-with-new-solution-for-ai-development-and-training-at-scale.html)
- [Shopify's Merlin](https://shopify.engineering/merlin-shopify-machine-learning-platform)


# ML workflow and automation frameworks

- [AWS SageMaker](https://aws.amazon.com/pm/sagemaker)
- [Collective Knowledge](https://github.com/mlcommons/ck)
- [CWL: common workflow language](https://www.commonwl.org)
- [Kedro](https://github.com/kedro-org/kedro)
- [Kubeflow](https://www.kubeflow.org)
- [MLFlow](https://mlflow.org/)
- [Redun: "yet another redundant workflow engine"]( https://github.com/insitro/redun )
- [ZenML: MLOps framework to create reproducible pipelines](https://github.com/zenml-io/zenml)

# Specifications

- [MLSpec](https://github.com/mlspec/MLSpec)

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

# ML containers

- ["COG" from Replicate](https://github.com/replicate/cog)
- [MLCube](https://github.com/mlcommons/mlcube)

# ML artifact management

- [CM toolkit](https://github.com/mlcommons/ck/tree/master/cm)


# Load testing tools

* [MLPerf loadgen](https://github.com/mlcommons/inference/tree/master/loadgen)
* [Locust - scalable user load testing tool written in Python](https://locust.io/)

# Misc tools

- [rclone](https://rclone.org) - rclone is a command-line program to manage files on cloud storage. It is a feature-rich alternative to cloud vendors' web storage interfaces.
