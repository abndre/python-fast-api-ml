from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


teste = []

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/value/me")
async def value_me():
    return {
        "value": "estou logado"
    }


@app.get("/value/{parameter}")
async def value(parameter: int):
    return {
        "value": parameter
    }

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/")
async def create_item(item: Item):
    teste.append(item)
    return "recebemos chefia"


@app.get("/items/")
async def create_item():
    return teste