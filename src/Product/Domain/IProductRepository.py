from abc import ABC, abstractmethod
from typing import List
from src.Product.Domain import Product



class IProductRepository(ABC):#This Interface will be later overloaded with an implementation of the Infrastructure layer

    @abstractmethod #Decorator
    def get_products(self) -> Product: # Retrieves the user based on the email
        pass
