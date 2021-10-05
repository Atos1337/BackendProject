import unittest
from typing import Dict

from database import Database
from service.book_service import BookService


class TestBookService(unittest.TestCase):
    class TestDatabase(Database):
        book_prices: Dict[str, float] = {
            "Граф Монте-Кристо": 1000
        }

    def setUp(self) -> None:
        self.bs = BookService(self.TestDatabase())

    def test_book_not_exist(self):
        self.assertIsNone(self.bs.get_book_price("не существует"))

    def test_book_exist(self):
        self.assertEqual(1000, self.bs.get_book_price("Граф Монте-Кристо"))


if __name__ == '__main__':
    unittest.main()
