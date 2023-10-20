import os
from fastapi.responses import JSONResponse
from kink import di
from fastapi import APIRouter, Depends
from src.Product.Domain.ProductErrors import ProductNotFoundException
from src.Product.Application.ProductService import ProductService
from src.shared.ILogger import ILogger

verbose = os.getenv('VERBOSE')
ProductRouter = APIRouter(
    prefix="/product",
    tags=["product"]
)# The router is a way to manage the different paths in a most organized way,


# # For now i will manage the service and logger as variables, is also possible to add it as params in every function/api call
# service:ProductService = Depends(lambda:di[ProductService])
# logger:ILogger = Depends(lambda:di[ILogger])

@ProductRouter.get("/")
def get_products(
    service:ProductService = Depends(lambda:di[ProductService]),
    logger:ILogger = Depends(lambda:di[ILogger])
) -> JSONResponse:
    products = []
    try:
        products =service.get_products()
        if verbose:
            logger.log_info("ROUTER: "+"Products found in the database")
    except ProductNotFoundException:
        if verbose:
            logger.log_error("ROUTER: "+"Products not found")
    return JSONResponse(status_code=200, content =products)


@ProductRouter.get("/{product_id}")
async def get_product(
    product_id:str,
    service:ProductService = Depends(lambda:di[ProductService]),
    logger:ILogger = Depends(lambda:di[ILogger])
    ):
    try:
        product =service.get_product(product_id)
        if verbose:
            logger.log_info("ROUTER: "+"Products found in the database")
    except ProductNotFoundException:
        if verbose:
            logger.log_error("ROUTER: "+"Products not found")
    return JSONResponse(status_code=200, content=product)