from src.Product.Domain.IProductRepository import IProductRepository
from src.Product.Domain.ProductErrors import ProductNotFoundException
from src.shared.ILogger import ILogger


class ProductService:
    def __init__(
        self,
        product_repo:IProductRepository,
        logger:ILogger,
        verbose:bool
    ) -> None:
        self.product_repo = product_repo
        self.logger = logger
        self.verbose = verbose

    def get_products(self):
        try:
            products = self.product_repo.get_products()
            if self.verbose:
                self.logger.log_info("Service: "+"Products found in the database")
        except ProductNotFoundException:
            if self.verbose:
                self.logger.log_error("Service: "+"Products not found")
            return []
        return products