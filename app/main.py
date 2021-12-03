from fastapi import FastAPI
from app.routers import item, models, value


app = FastAPI()
app.include_router(item.router)
app.include_router(models.router)
app.include_router(value.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


