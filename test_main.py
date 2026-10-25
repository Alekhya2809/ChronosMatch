
import unittest

from main import Order, match_orders


class TestOrderMatching(unittest.TestCase):

    def test_partial_fill(self):
        buy = Order(1, "BUY", 100.0, 10)
        sells = [Order(2, "SELL", 99.0, 5)]

        trades = match_orders(buy, sells)

        self.assertEqual(len(trades), 1)
        self.assertEqual(trades[0].quantity, 5)
        self.assertEqual(buy.quantity, 5)
        self.assertEqual(sells[0].quantity, 0)

    def test_no_match_when_buy_price_is_too_low(self):
        buy = Order(1, "BUY", 90.0, 10)
        sells = [Order(2, "SELL", 99.0, 5)]

        trades = match_orders(buy, sells)

        self.assertEqual(len(trades), 0)
        self.assertEqual(buy.quantity, 10)
        self.assertEqual(sells[0].quantity, 5)

    def test_match_multiple_sell_orders(self):
        buy = Order(1, "BUY", 100.0, 10)
        sells = [
            Order(2, "SELL", 98.0, 4),
            Order(3, "SELL", 99.0, 3),
        ]

        trades = match_orders(buy, sells)

        self.assertEqual(len(trades), 2)
        self.assertEqual(sum(t.quantity for t in trades), 7)
        self.assertEqual(buy.quantity, 3)
        self.assertEqual(sells[0].quantity, 0)
        self.assertEqual(sells[1].quantity, 0)
        
    def test_lowest_sell_price_is_matched_first(self):
        buy = Order(1, "BUY", 100.0, 10)
        sells = [
            Order(2, "SELL", 99.0, 4),
            Order(3, "SELL", 98.0, 3),
        ]

        trades = match_orders(buy, sells)

        self.assertEqual(trades[0].sell_order_id, 3)
        self.assertEqual(trades[0].price, 98.0)
        self.assertEqual(trades[0].quantity, 3)


if __name__ == "__main__":
    unittest.main()
