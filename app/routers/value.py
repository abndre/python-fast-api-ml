from fastapi import APIRouter
router = APIRouter()


@router.get("/value/me")
async def value_me():
    return {
        "value": "estou logado"
    }


@router.get("/value/{parameter}")
async def value(parameter: int):
    return {
        "value": parameter
    }