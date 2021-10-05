from database import Database


class BookService:
    def __init__(self, database: Database):
        self.db = database

    def get_book_price(self, book_name: str):
        return self.db.book_prices.get(book_name)
