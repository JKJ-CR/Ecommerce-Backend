import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.User.Infrastructure.UserRouter import UserRouter
from src.shared.errors import *

app = FastAPI()


app.include_router(UserRouter)


@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException) -> JSONResponse:
    error_msg = APIErrorMessage(type=exc.__class__.__name__, message=f"Oops! {exc}")
    return JSONResponse(
        status_code=400,
        content=error_msg.dict(),
    )

@app.exception_handler(ResourceNotFoundException)
async def resource_not_found_handler(request: Request, exc: ResourceNotFoundException) -> JSONResponse:
    error_msg = APIErrorMessage(type=exc.__class__.__name__, message=str(exc))
    return JSONResponse(status_code=404, content=error_msg.dict())


@app.exception_handler(RepositoryError)
async def repository_error_handler(request: Request, exc: RepositoryError) -> JSONResponse:
    error_msg = APIErrorMessage(
        type=exc.__class__.__name__, message="Oops! Something went wrong, please try again later..."
    )
    return JSONResponse(
        status_code=500,
        content=error_msg.dict(),
    )


if __name__ == "__main__":
    print("QUESO")
    uvicorn.run(app, host="localhost", port=3400)