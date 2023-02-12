from src.User.Application.UserDTO import CredentialsDTO
from src.User.Domain.IUserRepository import IUserRepository
from src.User.Domain.UserErrors import UserNotFoundException

class UserService:
    def __init__(
        self,
        user_repo:IUserRepository,
        ) -> None:
        self.user_repo = user_repo

    def login(self, imputDTO:CredentialsDTO)->bool:
        try:
            user = self.user_repo.get_user(imputDTO.email) # retrieves the user data

        except UserNotFoundException:
            return False
            
        return user.login(imputDTO.email,imputDTO.password)