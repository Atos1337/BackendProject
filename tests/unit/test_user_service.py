import unittest
from typing import Dict, Set
from service.user_service import UserService
from database import Database


class TestUserServiceIntersect(unittest.TestCase):
    class TestDatabase(Database):
        users_books: Dict[str, Set[str]] = {
            "Vitya": {
                "Граф Монте-Кристо",
                "Чиполлино"
            },
            "Vova": {
                "Граф Монте-Кристо",
                "Сеньор-Помидор"
            },
            "Vasya": {
                "Смешарики"
            }
        }

    def setUp(self) -> None:
        self.us = UserService(self.TestDatabase())

    def test_user_not_exist(self):
        self.assertIsNone(self.us.intersect_users_books("Valenok", "Vasya"))
        self.assertIsNone(self.us.intersect_users_books("Vasya", "Valenok"))

    def test_empty_intersect(self):
        self.assertEqual(set(), self.us.intersect_users_books("Vitya", "Vasya"))

    def test_not_empty_intersect(self):
        self.assertEqual({"Граф Монте-Кристо"}, self.us.intersect_users_books("Vova", "Vitya"))


if __name__ == '__main__':
    unittest.main()
