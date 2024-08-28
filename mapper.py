from models import ProductUpdateDataDTO, ProductUpdateData
from repository import Repository


def map_product_update_data_dto_to_product_update_data(
        repository: Repository, product_update_data_dto: ProductUpdateDataDTO) -> ProductUpdateData:
    category_id = repository.get_category_id_by_category_name(product_update_data_dto.category_name)
    map_dict = product_update_data_dto.__dict__
    map_dict.pop('category_name')
    return ProductUpdateData(**{**map_dict, "category_id": category_id})
