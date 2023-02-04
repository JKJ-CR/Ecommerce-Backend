from kink import di
from User.Domain.IUserRepository import IUserRepository

from User.Infrastructure.MongoUserRepository import MongoUserRepository
from configs.MongoDB import get_db_connection


def UserDI()->None:
    repository = MongoUserRepository( get_db_connection() )
    di[IUserRepository] =repository