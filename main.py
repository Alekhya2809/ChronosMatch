
from dataclasses import dataclass


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


def match_orders(buy_order, sell_orders):
    # Validate the buy order
    if buy_order.side != "BUY":
        print("The first order must be a BUY order.")
        return []

    if buy_order.quantity <= 0:
        print("Buy quantity must be positive.")
        return []

    trades = []

    # Try matching the buy order with each sell order
    for sell_order in sorted(sell_orders, key=lambda order: order.price):
        if buy_order.quantity == 0:
            break

        if sell_order.side != "SELL":
            print("Skipping an invalid sell order.")
            continue

        if sell_order.quantity <= 0:
            print("Skipping a sell order with invalid quantity.")
            continue

        # A trade is possible if the buy price covers the sell price
        if buy_order.price >= sell_order.price:
            traded_quantity = min(
                buy_order.quantity,
                sell_order.quantity
            )

            # Execute the trade at the seller's price
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
