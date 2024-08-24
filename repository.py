from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, Session
from models import Product, Category, ProductBase

DATABASE_URL = 'postgresql+psycopg2://postgres:12345@localhost/fast_api_magasin'


class Repository:
    def __init__(self):
        self.engine = create_engine(url=DATABASE_URL, echo=True)
        self.Base = declarative_base()

    def get_all_products(self):
        with Session(self.engine) as session:
            products = session.query(Product).all()
        print(products)
        return products

    def get_all_categories(self):
        with Session(self.engine) as session:
            categories = session.query(Category).all()
        print(categories)
        return categories
