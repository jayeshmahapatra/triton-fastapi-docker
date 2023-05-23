import requests
import gradio as gr
import base64
import cv2
import numpy as np


def encode_img_base64(image: np.ndarray) -> str:
    """Decode byte image with base64 to np.ndarray."""
    return base64.b64encode(image.tobytes()).decode("utf8")

def classify_image(img) -> str:
    img = img.reshape((-1, 224, 224, 3))

    #base64 encode image
    base64_img = encode_img_base64(img)

    #Height and Width are fixed
    height = 224
    width = 224

    url = 'http://fastapi:5000'
    route = '/predict'
    
    #Send a get request to fastapi server
    params = {'base64_image': base64_img,  
    'height': height,
    'width': width}

    try:
        response = requests.get(url + route, json= params, timeout=120)
        response = response.json()
        insect_name = str(response)
    except Exception as ex:
        return "Exception: " + str(ex)

    

    return insect_name


interface = gr.Interface(fn=classify_image, 
             inputs=gr.Image(shape=(224, 224)),
             outputs=["text"],
             examples=["ant.jpg", "bee.jpg"]
             )

interface.launch(server_name="0.0.0.0", server_port=8080)


