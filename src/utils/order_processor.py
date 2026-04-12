from main import (
    load_orders_from_file,
    process_orders,
    analyze_orders,
    OrderInfo,
    OrderStats,
)


def process_order_file(input_file: str, output_file: str) -> None:
    orders_data: list[str] = load_orders_from_file(input_file)
    processed_orders: list[OrderInfo] = process_orders(orders_data)
    stats: OrderStats = analyze_orders(processed_orders)

    with open(output_file, "a", encoding="UTF-8") as processed_orders_report:
        statuses_string: str = ", ".join(
            [f"{key}: {value}" for key, value in stats["by_status"].items()]
        )
        processed_orders_report.write(
            f"Обработано заказов:{stats["total_orders"]}\n\
Общая сумма: {stats["total_sum"]} руб.\n\
По статусам: {statuses_string}\n\
Уникальных пользователей: {len(stats["unique_users"])}\n\n"
        )
