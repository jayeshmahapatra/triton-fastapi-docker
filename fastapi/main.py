# fastapi
from fastapi import FastAPI

# triton client
import tritonclient.grpc.aio as grpcclient

# Pydantic Schemas
from schema import ClassificationRequest, ClassificationResult

# Numpy
import numpy as np

# Utils
from utils import decode_img_to_numpy

app = FastAPI()

async def test_infer(triton_client: grpcclient.InferenceServerClient, 
                     model_name: str, 
                     input_data: np.ndarray, 
                     input_node: str, 
                     output_node: str) -> grpcclient.InferResult:
    
    """
    Perform inference using Triton server client.

    Args:
        triton_client (grpcclient.InferenceServerClient): Triton server client.
        model_name (str): Name of the model to perform inference on.
        input_data (np.ndarray): Input data for inference.
        input_node (str): Input node name in the Triton model.
        output_node (str): Output node name in the Triton model.

    Returns:
        grpcclient.InferResult: Inference results from Triton server.
    """

    inputs = []
    outputs = []

    inputs.append(grpcclient.InferInput(input_node, input_data.shape, "FP32"))
    inputs[0].set_data_from_numpy(input_data)
    outputs.append(grpcclient.InferRequestedOutput(output_node))	
    results = await triton_client.infer(
        model_name,
        inputs,
        outputs = outputs
        )

    return results


@app.get("/")
async def root():
    """
    Default root endpoint.

    Returns:
        dict: A simple greeting message.
    """
    return {"message": "Hello World"}


@app.get("/predict", response_model=ClassificationResult)
async def predict(data: ClassificationRequest) -> ClassificationResult:
    """
    Perform prediction using the provided image data.

    Args:
        data (ClassificationRequest): Classification request containing image data.

    Returns:
        ClassificationResult: Classification result containing the predicted label.
    """

    # Decode base64 image into numpy array
    img = decode_img_to_numpy(data.base64_image, data.height, data.width)

    # Create a grpc InferenceServerClient to interface with the triton service
    triton_client = grpcclient.InferenceServerClient(url="triton:8001")

    # Do model inference and get results back
    triton_out = await test_infer(
        triton_client,
        model_name="bee_vs_ant",
        input_data=img,
        input_node="INPUT__0",
        output_node="OUTPUT__0"
    )

    # Cast model output as numpy
    logits = triton_out.as_numpy("OUTPUT__0")
    result = {}
    
    # Based on logits, the image is predicted to be of a bee or an ant
    result['prediction'] = "bee" if logits[0].argmax() == 1 else "ant"

    return result