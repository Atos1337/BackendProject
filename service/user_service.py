from database import Database
from util.calc import calc_actual_book_price_for_user
from service.book_service import BookService


class UserService:
    def __init__(self, database: Database, book_service: BookService = None):
        self.db = database
        self.bs = book_service

    def intersect_users_books(self, user1: str, user2: str):
        if user1 not in self.db.users_books or user2 not in self.db.users_books:
            return None
        else:
            return self.db.users_books[user1].intersection(self.db.users_books[user2])

    def is_can_user_buy(self, user_name: str, book_name: str, user_budget: float, book_promo: float = None):
        user_promo = self.db.users_promo.get(user_name)
        actual_price = calc_actual_book_price_for_user(self.bs.get_book_price(book_name), book_promo, user_promo)
        if not actual_price:
            return None
        else:
            return actual_price <= user_budget

    def buyable_books_intersect(self, buy_user: str, other_user: str, user_budget: float):
        books_intersect = self.intersect_users_books(buy_user, other_user)
        if not books_intersect:
            return None
        else:
            return set(filter(lambda book: self.is_can_user_buy(buy_user, book, user_budget) or False, books_intersect))
