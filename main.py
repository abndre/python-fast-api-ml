from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/value/{parameter}")
async def value(parameter: int):
    return {
        "value": parameter
    }

@app.get("/value")
async def value():
    return "alguma coisa devera ser passada"