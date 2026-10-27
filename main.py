
from dataclasses import dataclass
import math


@dataclass
class Order:
    order_id: int
    side: str
    price: float
    quantity: int


@dataclass
class Trade:
    buy_order_id: int
    sell_order_id: int
    price: float
    quantity: int


def is_valid_order(order, expected_side):
    """Check whether an order has valid values."""
    if order.side != expected_side:
        return False

    if isinstance(order.price, bool) or not isinstance(
        order.price, (int, float)
    ):
        return False

    if not math.isfinite(order.price) or order.price <= 0:
        return False

    if isinstance(order.quantity, bool) or not isinstance(
        order.quantity, int
    ):
        return False

    if order.quantity <= 0:
        return False

    return True


def match_orders(buy_order, sell_orders):
    # Validate the buy order
    if not is_valid_order(buy_order, "BUY"):
        print("Invalid buy order. Check its side, price, and quantity.")
        return []

    trades = []

    # Match the lowest-priced sell orders first
    for sell_order in sorted(sell_orders, key=lambda order: order.price):
        if buy_order.quantity == 0:
            break

        # Skip invalid sell orders
        if not is_valid_order(sell_order, "SELL"):
            print(
                f"Skipping invalid sell order #{sell_order.order_id}."
            )
            continue

        # A trade is possible if the buy price covers the sell price
        if buy_order.price >= sell_order.price:
            traded_quantity = min(
                buy_order.quantity,
                sell_order.quantity
            )

            trade = Trade(
                buy_order_id=buy_order.order_id,
                sell_order_id=sell_order.order_id,
                price=sell_order.price,
                quantity=traded_quantity
            )

            trades.append(trade)

            # Update remaining quantities
            buy_order.quantity -= traded_quantity
            sell_order.quantity -= traded_quantity

    return trades


def main():
    buy_order = Order(1, "BUY", 100.0, 10)

    sell_orders = [
        Order(2, "SELL", 98.0, 4),
        Order(3, "SELL", 99.0, 3),
    ]

    print("ChronosMatch - Order Matching Engine")
    print("------------------------------------")
    print("Initial buy order:", buy_order)

    for order in sell_orders:
        print("Sell order:", order)

    trades = match_orders(buy_order, sell_orders)

    print("\nTrade Results")
    print("------------------------------------")

    if trades:
        for trade in trades:
            print(
                f"Trade: BUY #{trade.buy_order_id} with "
                f"SELL #{trade.sell_order_id} | "
                f"Quantity: {trade.quantity} | "
                f"Price: {trade.price}"
            )
    else:
        print("No trades executed.")

    print("\nRemaining buy quantity:", buy_order.quantity)

    for order in sell_orders:
        print(
            f"Remaining quantity for SELL #{order.order_id}:",
            order.quantity
        )


if __name__ == "__main__":
    main()
