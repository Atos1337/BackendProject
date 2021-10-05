from database.in_memory_db import InMemoryDatabase
from service.user_service import UserService
from service.book_service import BookService

in_memory_db = InMemoryDatabase()
bs = BookService(in_memory_db)
us = UserService(in_memory_db, bs)
