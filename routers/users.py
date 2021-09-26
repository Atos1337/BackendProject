from fastapi import APIRouter, Query, HTTPException
from models.requests.can_buy_request import CanBuyRequest
from database.in_memory_db import book_prices

router = APIRouter()


@router.get("/hello")
async def hello_user(user_name: str = Query(..., alias="user-name", regex="^[a-zA-Z]+$")):
    return {"message": "Hello World, {}!".format(user_name)}


@router.post("/book/can-buy")
async def is_user_can_buy(can_buy_request: CanBuyRequest):
    if can_buy_request.book_name not in book_prices:
        raise HTTPException(status_code=404, detail="That book does not exist")
    else:
        actual_price = book_prices[can_buy_request.book_name] * can_buy_request.actual_price_with_promo
        if can_buy_request.user_budget >= actual_price:
            return {"message": "Can buy {} for {}".format(can_buy_request.book_name, actual_price)}
        else:
            return {"message": "Can not buy {}".format(can_buy_request.book_name)}
