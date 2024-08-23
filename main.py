from fastapi import FastAPI
import repository
from models import ProductBase

app = FastAPI()
repo = repository.Repository()


@app.get("/")
async def root():
    return {"message": "app"}


@app.get("/get_products", response_model=list[ProductBase])
async def get_products():
    products = repo.get_all_products()
    return products
