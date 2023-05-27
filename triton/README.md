# Triton Service

This is the readme for the Triton service. The Triton service is part of the triton-fastapi-docker repository and is responsible for running the NVIDIA Triton inference engine to serve machine learning models. It utilizes the Triton Docker image from `nvcr.io/nvidia/tritonserver:22.12-py3`.

## Folder Structure

The Triton service folder has the following structure:

```
triton/
├── Dockerfile
└── model_repository/
    └── {model_name}/
        ├── config.pbtxt
        └── {version}/
            └── {model_files}
```

- **Dockerfile**: The `Dockerfile` in the triton folder is used to build the Triton container. It specifies the necessary dependencies and configurations to run the Triton service.

- **model_repository**: The `model_repository` subfolder contains machine learning models that the Triton service deploys. Each model is organized into its own folder.

## Model Configuration

Within each model folder in the `model_repository`, there is a `config.pbtxt` file that contains the configuration details for the model. It specifies information like:
- The input and output tensor shapes
- Whether the model runs on CPU or GPU 
- The number of parallel instances of the model to load.

The file path for the model configuration is as follows:

```
triton/model_repository/{model_name}/config.pbtxt
```
More information about the config.pbxt format can be found in this [link](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md).

## Model Versions

Each model folder can have multiple version subfolders, where each version is indicated by a natural number. For example, the following structure represents a model named `bee_vs_ant` with a single version:

```
triton/model_repository/bee_vs_ant/1/
```

Within the version folder, the actual model files are stored. These model files can be in any format supported by Triton, such as ONNX, TorchScript, Tensorflow, TensorRT etc.

## Usage

To use the Triton service, follow the instructions in the main repository's readme: [triton-fastapi-docker](https://github.com/jayeshmahapatra/triton-fastapi-docker).