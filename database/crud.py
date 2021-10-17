from sqlalchemy.orm import Session

from database import models, schemas


def get_book_offer(db: Session, book_offer_id: int):
    return db.query(models.BookOffer).filter(models.BookOffer.id == book_offer_id).first()


def get_book_offers_by_book_title(db: Session, book_title: str, limit: int = 10):
    return db.query(models.BookOffer).filter(models.BookOffer.book_title == book_title).limit(limit).all()


def create_book_offer(db: Session, book_offer: schemas.BookOfferCreate):
    db_book_offer = models.BookOffer(
        book_title=book_offer.book_title,
        book_price=book_offer.book_price,
        shop_url=book_offer.shop_url
    )
    db.add(db_book_offer)
    db.commit()
    db.refresh(db_book_offer)
    return db_book_offer

