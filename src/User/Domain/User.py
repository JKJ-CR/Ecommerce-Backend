from pydantic import EmailStr


class User:
    def __init__(
            self, id: str, name: str, email: EmailStr, password: str
    ) -> None:
        self._name = name
        self._email = email
        self._password = password
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> EmailStr:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @property
    def id(self) -> str:
        return self._id

    def login(self, email: EmailStr, password: str) -> bool:
        return True if self._email == email and self._password == password else False

