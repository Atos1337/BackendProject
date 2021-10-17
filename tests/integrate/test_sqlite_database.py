import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from routers.market import get_db
from database.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_book_offer(test_db):
    response = client.post(
        "/book-offers/",
        json={
            "book_price": 1000,
            "book_title": "Граф Монте-Кристо",
            "shop_url": "test.url"
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["book_price"] == 1000
    assert "id" in data
    book_offer_id = data["id"]

    response = client.get(f"/book-offers/{book_offer_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["book_price"] == 1000
    assert data["book_title"] == "Граф Монте-Кристо"
    assert data["shop_url"] == "test.url"
    assert data["id"] == book_offer_id
