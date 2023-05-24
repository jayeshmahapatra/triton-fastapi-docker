import requests
import gradio as gr
import base64
import numpy as np


def encode_img_base64(image: np.ndarray) -> str:
    """Decode byte image with base64 to np.ndarray."""
    return base64.b64encode(image.tobytes()).decode("utf8")

def classify_image(img: np.ndarray) -> str:
    """
    Classifies an image as either an 'ant' or a 'bee' using a FastAPI server.

    Args:
        img (np.ndarray): The image to be classified.

    Returns:
        str: The name of the insect ('ant' or 'bee').
    """

    # Reshape the image to the desired dimensions
    img = img.reshape((-1, 224, 224, 3))

    # Base64 encode the image
    base64_img = encode_img_base64(img)

    # Define the fixed height and width of the image
    height = 224
    width = 224

    # Set the URL and route for the FastAPI server
    url = 'http://fastapi:5000'
    route = '/predict'
    
    # Prepare the parameters for the request
    params = {'base64_image': base64_img,  
    'height': height,
    'width': width}

    try:
        # Send a GET request to the FastAPI server with the image data
        response = requests.get(url + route, json= params, timeout=120)
        
        # Get the JSON response from the server
        response = response.json()

        # Extract the insect name from the response
        insect_name = str(response)
    except Exception as ex:
        # Return an error message if an exception occurs
        return "Exception: " + str(ex)

    

    return insect_name


interface = gr.Interface(fn=classify_image, 
             inputs=gr.Image(shape=(224, 224)),
             outputs=["text"],
             examples=["ant.jpg", "bee.jpg"]
             )

interface.launch(server_name="0.0.0.0", server_port=8080)


