#fastapi
from fastapi import FastAPI

#triton client
import tritonclient.grpc.aio as grpcclient

#Pydantic Schemas
from schema import ClassificationRequest, ClassificationResult

#Numpy
import numpy as np

#Utils
from utils import decode_img_to_numpy
import sys

app = FastAPI()

async def test_infer(triton_client,
                    model_name,
                    input_data,
                    input_node, 
                    output_node
):
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
    return {"message": "Hello World"}

@app.get("/predict", response_model=ClassificationResult)
async def predict(data: ClassificationRequest) -> ClassificationResult:

    img = decode_img_to_numpy(data.base64_image, data.height, data.width)
    #img = np.random.rand(1,3,224,224).astype(np.float32)
    triton_client = grpcclient.InferenceServerClient(url= "triton:8001")
    triton_out = await test_infer(triton_client, model_name= "bee_vs_ant", input_data= img,
                                input_node = "INPUT__0", output_node = "OUTPUT__0")
    logits = triton_out.as_numpy("OUTPUT__0")

    result = {}
    
    result['prediction'] = "bee" if logits[0].argmax() == 1 else "ant"

    return result