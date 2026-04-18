from models.product import Product
from models.user import User
from models.exceptions import ValidationError, BusinessLogicError


class Order:
    def __init__(
        self, order_id: int, total: float, user: User, products: list[Product]
    ):
        """Создает заказ"""
        self._order_id: int = order_id
        self._total: float = total
        self._user: User = user

        if len(products) == 0:
            raise BusinessLogicError("Пустой список товаров в заказе")
        self._products: list[Product] = products

    def add_product(self, product: Product) -> None:
        """Добавить продукт к заказу"""
        if not isinstance(product, Product):
            raise ValidationError("Товар должен быть объектом класса Product")
        self._products.append(product)

    def calculate_total(self) -> float:
        """Получить стоимость заказа"""
        total_price: float = 0.0
        for product in self._products:
            total_price += product.get_total_price()

        total_price_rounded: float = round(total_price, 2)
        return total_price_rounded

    def remove_product(self, product_name: str):
        """Удалить продукт из заказа"""
        index_to_delete: int = -1
        for product_i, product in enumerate(self._products):
            if product.name == product_name:
                index_to_delete = product_i
                break
        if index_to_delete != -1:
            del self._products[index_to_delete]
            return
        raise BusinessLogicError("Товар не найден")

    def __str__(self) -> str:
        return f"Заказ пользователя {self._user.name} на сумму " f"{self._total} руб."
