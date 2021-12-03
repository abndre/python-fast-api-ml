from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
router = APIRouter()

teste = []


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@router.post("/items/")
async def create_item(item: Item):
    teste.append(item)
    return "recebemos chefia"


@router.get("/items/")
async def create_item():
    return teste