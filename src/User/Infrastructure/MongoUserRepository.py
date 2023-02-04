from User.Domain.User import User
from User.Domain.IUserRepository import IUserRepository
from shared.errors import RepositoryError
from pymongo.database import Database
from pymongo.errors import PyMongoError
from typing import Mapping , Any

from User.Domain.UserErrors import UserNotFoundException

MongoDocument = Mapping[str, Any] # Defined just to make easier the understanding of some annotations


class MongoUserRepository(IUserRepository):

    def __init__(self,database:Database):
        self._collection = database.get_collection("users")

    def to_entity(self, document:MongoDocument)->User:# Convert a MongoDocument to an entity (User)
        return User(
            _id = document["_id"],
            name = document["name"],
            email = document["email"],
            password = document["password"]
        )



    def get_user(self,email:str)-> User:
        try:
            document = self._collection.find_one( {"email":email} )

            if not document:# that means the database was unable to find the user an undefind value is returned

                raise UserNotFoundException(f"User with email: {email} was not found")

        except PyMongoError as error:

            raise RepositoryError.get_operation_failed()

        return self.to_entity(document)
    

