import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def process_order(order_id: int) -> str:
    logging.info(f"Processing order {order_id}")
    return f"Order {order_id} processed"


if __name__ == "__main__":
    print(process_order(101))