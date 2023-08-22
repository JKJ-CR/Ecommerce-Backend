from src.Product.Domain.IProductRepository import IProductRepository
import requests

class DummyProductRepository(IProductRepository):
    def __init__(self) -> None:
        pass

    def get_products(self):
        result = []
        try:
            r = requests.get('https://dummyjson.com/products')
        except Exception:
            r = []
        return r.json()
        

