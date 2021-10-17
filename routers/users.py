from fastapi import APIRouter, Query, HTTPException
from models.requests.can_buy_request import CanBuyRequest
from dependencies import us

router = APIRouter()


@router.get("/hello")
async def hello_user(user_name: str = Query(..., alias="user-name", regex="^[a-zA-Z]+$")):
    return {"message": "Hello World, {}!".format(user_name)}


@router.post("/user/can-buy")
async def is_user_can_buy(can_buy_request: CanBuyRequest):
    user_can_buy = us.is_can_user_buy(
        can_buy_request.user_name,
        can_buy_request.book_name,
        can_buy_request.user_budget,
        can_buy_request.actual_price_with_promo
    )
    if user_can_buy is None:
        raise HTTPException(status_code=404, detail="User or book can not found")
    if user_can_buy:
        return {"message": "Can buy {}".format(can_buy_request.book_name)}
    else:
        return {"message": "Can not buy {}".format(can_buy_request.book_name)}


@router.get("/user/book_intersect")
async def users_book_intersect(user_name1: str = Query(..., alias="user-name1", regex="^[a-zA-Z]+$"),
                               user_name2: str = Query(..., alias="user-name2", regex="^[a-zA-Z]+$")):
    books_intersect = us.intersect_users_books(user_name1, user_name2)
    if books_intersect is None:
        raise HTTPException(status_code=404, detail="One of users not found")
    return books_intersect


@router.get("/user/buyable_book_intersect")
async def buyable_books_intersect(buy_user: str = Query(..., alias="buy-user", regex="^[a-zA-Z]+$"),
                                  other_user: str = Query(..., alias="other-user", regex="^[a-zA-Z]+$"),
                                  user_budget: float = Query(..., alias="user-budget", gt=0)):
    res = us.buyable_books_intersect(buy_user, other_user, user_budget)
    if res is None:
        raise HTTPException(status_code=404, detail="One of users not found")
    return res
