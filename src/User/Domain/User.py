from pydantic import EmailStr

class User:
    def __init__(
        self, _id: str, name:str, email:EmailStr, password:str,
        ) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.id = _id


    @property
    def name(self)->str:
        return self.name

    @property
    def email(self)->EmailStr:
        return self.email
    
    @property
    def password(self)->str:
        return self.password

    @property
    def id(self)->str:
        return self.id

    def login(self,email:EmailStr, password:str)->bool:
        return True if self.email == email and self.password == password else False
        
    