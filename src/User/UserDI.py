from kink import di

from src.User.Application.UserService import UserService
from src.User.Domain.IUserRepository import IUserRepository
from src.User.Infrastructure.MongoUserRepository import MongoUserRepository
from src.configs.MongoDB import get_db_connection


def UserDI()->None:
    repository = MongoUserRepository( get_db_connection() )
    di[IUserRepository] =repository
    di[UserService] = UserService(repository)