from fastapi import APIRouter, Depends
from kink import di

from src.User.Application.UserDTO import CredentialsDTO
from src.User.Application.UserService import UserService

UserRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)# The router is a way to manage the different paths in a most organized way,
# if the server reads a /users request will come directly to this router and check its methods


@UserRouter.get("/")# Call the definition of the user Router and the HTTP method GET
def login():
    return {"username": "test", "password": "test"}

@UserRouter.post(
    "/login",
response_model=bool)
def login(
    request:CredentialsDTO,
    service:UserService = Depends(lambda:di[UserService])
    )-> bool:
    return service.login(request)