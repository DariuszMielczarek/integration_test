from typing import Annotated

from fastapi import FastAPI, Path, Body
from starlette.middleware.cors import CORSMiddleware
import repository
from mapper import map_product_update_data_dto_to_product_update_data
from models import ProductBase, CategoryBase, ProductUpdateDataDTO

app = FastAPI()
repo = repository.Repository()

origins = ['http://localhost:3000',
           'http://localhost:8080'
           'http://192.168.30.52:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "app"}


@app.get("/products", response_model=list[ProductBase])
async def get_products():
    products = repo.get_all_products()
    return products


@app.put("/products/{product_name}", response_model=ProductBase)
async def update_product(product_name: Annotated[str, Path()],
                         product_update_data_dto: Annotated[ProductUpdateDataDTO, Body()]):
    print(product_update_data_dto)
    product_update_data = map_product_update_data_dto_to_product_update_data(repo, product_update_data_dto)
    updated_product = repo.update_product(product_name, product_update_data)
    return updated_product


@app.get("/categories", response_model=list[CategoryBase])
async def get_categories():
    categories = repo.get_all_categories()
    return categories
