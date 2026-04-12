from models.exceptions import ValidationError


class User:
    def __init__(self, name: str, email: str):
        self._name: str = name

        if "@" not in email:
            raise ValidationError("Неверный формат email")
        self._email = email

    def get_info(self) -> str:
        return f"Пользователь: {self._name}, Email: {self._email}"

    def set_email(self, email: str) -> None:
        if "@" not in email:
            raise ValidationError("Неверный формат email")
        self._email = email

    def get_email(self) -> str:
        return self._email
