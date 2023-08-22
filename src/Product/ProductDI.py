from kink import di
from src.Product.Application.ProductService import ProductService
from src.Product.Domain import IProductRepository
from src.Product.Infrastructure.DummyProductRepository import DummyProductRepository

from src.configs.MongoDB import get_db_connection
from src.shared.LocalLogger import LocalLogger
import os

from src.shared.ILogger import ILogger


def ProductDI()->None:
    repository = DummyProductRepository()
    logger = LocalLogger()
    VERBOSE = os.getenv("VERBOSE")
    di[ILogger] = logger
    di[IProductRepository] =repository
    di[ProductService] = ProductService(repository,logger,VERBOSE )