from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import repository
from models import ProductBase, CategoryBase

app = FastAPI()
repo = repository.Repository()

origins = ['http://localhost:8000',
           'http://192.168.30.36:8000']

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


@app.get("/categories", response_model=list[CategoryBase])
async def get_categories():
    categories = repo.get_all_categories()
    return categories
