from models.exceptions import ValidationError


class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str):
        if price < 0.0:
            raise ValidationError("Цена не может быть отрицательной")
        self._price: float = price

        self._name: str = name
        self._quantity: int = quantity
        self._category = category

    def get_total_price(self) -> float:
        """Посчитать текущую цену"""
        return self._price * self._quantity

    def set_price(self, price):
        """Установить цену"""
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self._price = price

    def calculate_shipping(self) -> float:
        return max(round(0.01 * self.price, 2), 300.0)

    def apply_discount(self, discount: float):
        if discount < 0.0 or discount > 1.0:
            raise ValidationError("Скидка долна быть в пределах 0.0 - 1.0")
        self._price = self._price * (1 - discount)

    def get_category(self) -> str:
        return self._category

    def check_stock(self):
        return self._quantity

    def update_stock(self, new_quantity):
        if new_quantity < 0:
            raise ValidationError("Количество не может быть отрицательным")
        self._quantity = new_quantity

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def __str__(self):
        return f"Товар: {self._name}, Цена: {self._price} руб., Количество: {self._quantity}"

    def __repr__(self):
        return f"Product('{self._name}', {self._price}, {self._quantity})"

    def __lt__(self, other: "Product") -> bool:
        if isinstance(other, Product):
            return self._price < other.price
        return False

    def __eq__(self, other: "Product") -> bool:
        if isinstance(other, Product):
            return self._price == other.price and self._name == other.name
        return False
