import json
import inflection
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Category, Product, Base

DATABASE_URL = 'postgresql+psycopg2://postgres:12345@localhost/fast_api_magasin'

engine = create_engine(url=DATABASE_URL, echo=True)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
        

def convert_keys(obj):
    if isinstance(obj, dict):
        return {inflection.underscore(k): convert_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys(i) for i in obj]
    else:
        return obj


with open('../shared-gd-products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    data = convert_keys(data)
    print(data)

with Session(engine) as session:
    for product in data:
        category_data = product.pop('category')

        category = session.query(Category).filter_by(category_id=category_data['category_id']).first()
        if not category:
            category = Category(**category_data)
            session.add(category)
            session.commit()

        product = Product(**product)
        session.add(product)

    session.commit()
