import unittest
from util.calc import calc_actual_book_price_for_user


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.book_price = 1000
        self.book_promo = 0.7
        self.user_promo = 0.5

    def test_none_book_price(self):
        self.assertIsNone(calc_actual_book_price_for_user(None, 0.5, 0.5))

    def test_none_promos(self):
        self.assertEqual(self.book_price, calc_actual_book_price_for_user(self.book_price, None, None))

    def test_none_one_promo(self):
        self.assertEqual(self.book_price * self.book_promo, calc_actual_book_price_for_user(
            self.book_price, self.book_promo, None
        ))
        self.assertEqual(self.book_price * self.user_promo, calc_actual_book_price_for_user(
            self.book_price, None, self.user_promo
        ))

    def test_not_none_promos(self):
        self.assertEqual(self.book_price * self.user_promo, calc_actual_book_price_for_user(
            self.book_price, self.book_promo, self.user_promo
        ))



if __name__ == '__main__':
    unittest.main()
