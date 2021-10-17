from sqlalchemy import Column, Integer, String, Float

from database.database import Base


class BookOffer(Base):
    __tablename__ = "book_offers"

    id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String, index=True)
    book_price = Column(Float, index=True)
    shop_url = Column(String, index=True)
