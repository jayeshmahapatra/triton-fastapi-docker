'''Pyantic schema for inference request and response'''
from pydantic import BaseModel, Field
from enum import Enum

class ClassificationRequest(BaseModel):

    base64_image: str = Field(...,title='Base64 encoded string', example = "GHJSDJS")
    height: int = Field(...,
                        title= "Height on the encoded image",
                        gt=0,  #Height must me greater than zero
                        example = 224)
    width: int = Field(...,
                       title= "Width of the encoded image",
                       gt=0, #Width must me greater than zero
                       example = 224)
    
class AnimalType(str, Enum):
    bee = 'bee'
    ant = 'ant'

class ClassificationResult(BaseModel):
    prediction: AnimalType = Field(...,title="Classification Result", example = "bee")

