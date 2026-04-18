from models.exceptions import ValidationError


class User:
    def __init__(self, name: str, email: str):
        """Создать пользователя"""
        self._name: str = name

        if "@" not in email:
            raise ValidationError("Неверный формат email")
        self._email = email

    def get_info(self) -> str:
        """Получить информацию о пользователе"""
        return f"Пользователь: {self._name}, Email: {self._email}"

    def set_email(self, email: str) -> None:
        """Изменить email"""
        if "@" not in email:
            raise ValidationError("Неверный формат email")
        self._email = email

    def get_email(self) -> str:
        """Получить email"""
        return self._email
