# triton-fastapi-docker

This repository demonstrates how to use NVIDIA Triton to deploy and serve ML models. It provides a set of services packaged in Docker containers that work together to serve a model capable of distinguishing between bees and ants.

## Prerequisites

Before getting started, ensure that you have the following prerequisites:

- Docker: You need to have Docker installed on your system to run the services. You can download and install Docker from the official Docker website: [https://www.docker.com/get-docker](https://www.docker.com/get-docker)

## Services

### 1. triton

The `triton` service runs the NVIDIA Triton inference engine and serves the ML model. It is responsible for handling the inference requests and providing predictions based on the input data.

### 2. fastapi

The `fastapi` service is a Python backend that communicates with the `triton` service using gRPC. It acts as an intermediary between the client and the `triton` service. Clients can send REST API requests to this service to predict whether an image contains a bee or an ant.

### 3. gradio

The `gradio` service provides a user-friendly interface using Gradio, which allows users to perform ML inference by uploading images. This interface sends API requests to the `fastapi` service for ML inference, which in turn communicates with the `triton` server to obtain the predictions.

## Usage

To get started, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/jayeshmahapatra/triton-fastapi-docker.git
   ```

2. Navigate to the `triton-fastapi-docker` directory:
   ```bash
   cd triton-fastapi-docker
   ```

3. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

   This command will start all three services: `triton`, `fastapi`, and `gradio`.

4. Once the services are up and running, you can access the Gradio interface by visiting `localhost:8080` in your web browser. The interface allows you to upload images and receive predictions on whether they contain bees or ants.

## Notebooks

The `notebooks` directory contains a Jupyter notebook that guides you through the process of creating a TorchScript model to distinguish between bee_vs_ant. It was used to create the model served by the triton service. If you want to train your own model, you can look at the notebook for reference.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This repository is licensed under the MIT License, except the contents of the **notebooks** folder which are licensed using BSD 3-Clause License. See the [LICENSE](LICENSE) file for more information.
