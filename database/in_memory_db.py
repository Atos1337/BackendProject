from database import Database
from typing import Dict, Set


class InMemoryDatabase(Database):
    book_prices: Dict[str, float] = {
        "Граф Монте-Кристо": 1000
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

    author_books: Dict[str, Set[str]] = {
        "Александр Дюма": {
            "А", "Б", "В", "Г"
        }
    }

    books_rating: Dict[str, float] = {
        "А": 5,
        "Б": 10,
        "В": 9,
        "Г": 8
    }
