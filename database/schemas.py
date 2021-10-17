from pydantic import BaseModel


class BookOfferBase(BaseModel):
    book_price: float
    book_title: str
    shop_url: str


class BookOfferCreate(BookOfferBase):
    pass


class BookOffer(BookOfferBase):
    id: int

    class Config:
        orm_mode = True
