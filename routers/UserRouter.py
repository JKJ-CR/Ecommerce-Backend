from fastapi import APIRouter

UserRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)


@UserRouter.get("/")
def login():
    return {"username": "test", "password": "test"}