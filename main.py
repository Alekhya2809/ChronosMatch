
from dataclasses import dataclass


@dataclass
class Order:
    order_id: int
    side: str
    price: float
    quantity: int


def match_orders(buy_order, sell_order):
    # Check whether the orders are valid for matching
    if buy_order.side != "BUY":
        print("First order must be a BUY order.")
        return

    if sell_order.side != "SELL":
        print("Second order must be a SELL order.")
        return

    if buy_order.quantity <= 0 or sell_order.quantity <= 0:
        print("Order quantities must be positive.")
        return

    # A trade is possible when the buy price covers the sell price
    if buy_order.price >= sell_order.price:
        traded_quantity = min(
            buy_order.quantity,
            sell_order.quantity
        )

        trade_price = sell_order.price

        # Update the remaining quantities
        buy_order.quantity -= traded_quantity
        sell_order.quantity -= traded_quantity

        print("\nTrade Executed!")
        print("-------------------------")
        print("Trade quantity:", traded_quantity)
        print("Trade price:", trade_price)
        print("Remaining buy quantity:", buy_order.quantity)
        print("Remaining sell quantity:", sell_order.quantity)
    else:
        print("\nNo trade: buy price is lower than sell price.")


def main():
    buy_order = Order(
        order_id=1,
        side="BUY",
        price=100.0,
        quantity=10
    )

    sell_order = Order(
        order_id=2,
        side="SELL",
        price=99.0,
        quantity=5
    )

    print("ChronosMatch - Order Matching Engine")
    print("------------------------------------")

    print("Buy order:", buy_order)
    print("Sell order:", sell_order)

    match_orders(buy_order, sell_order)


if __name__ == "__main__":
    main()

