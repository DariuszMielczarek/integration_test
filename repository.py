from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import declarative_base, Session
from models import Product, Category, ProductUpdateData

DATABASE_URL = 'postgresql+psycopg2://postgres:12345@localhost/fast_api_magasin'


class Repository:
    def __init__(self):
        self.engine = create_engine(url=DATABASE_URL, echo=True)
        self.Base = declarative_base()

    def get_all_products(self):
        with Session(self.engine) as session:
            products = session.query(Product).order_by(Product.product_id).all()
        print(products)
        return products

    def get_all_categories(self):
        with Session(self.engine) as session:
            categories = session.query(Category).order_by(Category.category_id).all()
        print(categories)
        return categories

    def update_product(self, product_name, product_update_data: ProductUpdateData):
        update_values = {key: value for key, value in vars(product_update_data).items() if value is not None}
        statement = update(Product).where(Product.product_name == product_name).values(**update_values)
        with Session(self.engine) as session:
            session.execute(statement)
            session.commit()
        return self.get_product_by_name(product_update_data.product_name
                                        if product_update_data.product_name else product_name)

    def get_product_by_name(self, product_name):
        statement = select(Product).where(Product.product_name == product_name).limit(1)
        with Session(self.engine) as session:
            fetched = session.execute(statement).fetchall()
            print('fffffff' + str(fetched))
        return fetched[0][0] if fetched else None

    def get_category_id_by_category_name(self, category_name) -> int | None:
        statement = select(Category.category_id).where(Category.category_name == category_name).limit(1)
        with Session(self.engine) as session:
            fetched = session.execute(statement).fetchall()
        return fetched[0][0] if fetched else None
