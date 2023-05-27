# Gradio Service

The Gradio service provides a user-friendly interface using Gradio, allowing users to perform machine learning inference by uploading images. This service communicates with the FastAPI service to request inferences for the uploaded images.

For instructions on running the Gradio service and the entire application, please refer to the [root readme](../README.md) of this repository.

## Folder Structure

The Gradio service folder has the following structure:

```
gradio/
├── app.py
├── example_images/
│   ├── ant.jpg
│   └── bee.jpg
├── Dockerfile
└── requirements.txt
```

- **app.py**: The `app.py` file contains the Gradio code to define the interface that the user interacts with when running the application. Users can use the interface to submit pictures for inference. This service then communicates with the FastAPI service to request inferences.

- **example_images**: The `example_images` folder contains example images of an ant and a bee. These images are shown as example inference queries in the Gradio interface, providing users with an understanding of the expected input format.

- **Dockerfile**: The `Dockerfile` in the Gradio folder is used to build the Gradio service container. It specifies the necessary dependencies and configurations to run the Gradio service.

- **requirements.txt**: The `requirements.txt` file lists the Python library requirements for running the Gradio service. These requirements are used during the Docker build process to ensure all necessary dependencies are installed.