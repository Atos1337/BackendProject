import unittest
from database import Database
from typing import Dict, Set

from service.book_service import BookService
from service.user_service import UserService


class TestDatabase(Database):
    book_prices: Dict[str, float] = {
        "Граф Монте-Кристо": 1000,
        "Простоквашино": 500
    }

    users_promo: Dict[str, float] = {
        "Vitya": 0.5
    }

    users_books: Dict[str, Set[str]] = {
        "Vitya": {
            "Граф Монте-Кристо",
            "Чиполлино"
        },
        "Vova": {
            "Граф Монте-Кристо",
            "Сеньор-Помидор"
        }
    }


class TestUserServiceCanUserBy(unittest.TestCase):
    def setUp(self) -> None:
        db = TestDatabase()
        bs = BookService(db)
        self.us = UserService(db, bs)

    def test_book_not_exist(self):
        self.assertIsNone(self.us.is_can_user_buy("Vitya", "не сущ", 1000, 0.5))

    def test_user_can_buy(self):
        self.assertEqual(True, self.us.is_can_user_buy("Vova", "Граф Монте-Кристо", 401, 0.4))

    def test_user_can_not_buy(self):
        self.assertEqual(False, self.us.is_can_user_buy("Vitya", "Граф Монте-Кристо", 499, 0.6))


class TestUserServiceBuyableBooksIntersect(unittest.TestCase):
    def setUp(self) -> None:
        db = TestDatabase()
        bs = BookService(db)
        self.us = UserService(db, bs)

    def test_none_intersect(self):
        self.assertIsNone(self.us.buyable_books_intersect("Не сушествующий", "Vitya", 1000))

    def test_empty_buyable_intersect_but_not_empty_usual_intersect(self):
        self.assertEqual(set(), self.us.buyable_books_intersect("Vitya", "Vova", 499))

    def test_not_empty_buyable_intersect(self):
        self.assertEqual({"Граф Монте-Кристо"}, self.us.buyable_books_intersect("Vitya", "Vova", 500))

if __name__ == '__main__':
    unittest.main()
