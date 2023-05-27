# FastAPI Service

The FastAPI service is responsible for running the Python backend that communicates with the Triton service using gRPC. It acts as an intermediary between the client and the Triton service. The FastAPI service receives REST API requests, processes them, and sends the predictions back to the client.

For instructions on running the FastAPI service and the entire application, please refer to the [root readme](../README.md) of this repository.

## Folder Structure

The FastAPI service folder has the following structure:

```
fastapi/
├── main.py
├── schema.py
├── utils.py
├── Dockerfile
└── requirements.txt
```

- **main.py**: The `main.py` file contains the FastAPI code with REST API routes to receive inference requests. It handles the incoming requests, processes them, and sends the data to the Triton service for inference.

- **schema.py**: The `schema.py` file contains the Pydantic model definitions. It defines the structure of the inference request that `main.py` receives and the structure of the response that `main.py` sends after processing the API request.

- **utils.py**: The `utils.py` file contains utility functions used by `main.py`. These utility functions may include data preprocessing, result formatting, or any other necessary helper functions.

- **Dockerfile**: The `Dockerfile` in the FastAPI folder is used to build the FastAPI service container. It specifies the necessary dependencies and configurations to run the FastAPI service using Gunicorn for parallelism.

- **requirements.txt**: The `requirements.txt` file lists the Python library requirements for running the FastAPI service. These requirements are used while building the Docker image to ensure all necessary dependencies are installed.