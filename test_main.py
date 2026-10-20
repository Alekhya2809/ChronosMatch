
import unittest

from main import Order, match_orders


class TestOrderMatching(unittest.TestCase):

    def test_matching_orders(self):
        buy = Order(1, "BUY", 100.0, 10)
        sell = Order(2, "SELL", 99.0, 5)

        match_orders(buy, sell)

        self.assertEqual(buy.quantity, 5)
        self.assertEqual(sell.quantity, 0)

    def test_no_match_when_buy_price_is_too_low(self):
        buy = Order(1, "BUY", 90.0, 10)
        sell = Order(2, "SELL", 99.0, 5)

        match_orders(buy, sell)

        self.assertEqual(buy.quantity, 10)
        self.assertEqual(sell.quantity, 5)


if __name__ == "__main__":
    unittest.main()
