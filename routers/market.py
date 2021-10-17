from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import models, schemas, crud
from database.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/book-offers/", response_model=schemas.BookOffer)
def create_book_offer(user: schemas.BookOfferCreate, db: Session = Depends(get_db)):
    return crud.create_book_offer(db, user)


@router.get("/book-offers/{book_offer_id}", response_model=schemas.BookOffer)
def get_book_offer(book_offer_id: int, db: Session = Depends(get_db)):
    db_book_offer = crud.get_book_offer(db, book_offer_id)
    if db_book_offer is None:
        raise HTTPException(status_code=404, detail="Book offer not found")
    return db_book_offer


@router.get("/book-offers/book-title/{book_title}", response_model=List[schemas.BookOffer])
def get_book_offers_by_book_title(book_title: str, db: Session = Depends(get_db)):
    book_offers = crud.get_book_offers_by_book_title(db, book_title)
    return book_offers
