from fastapi import FastAPI, Query, Response, status
from pydantic import BaseModel, Field


class CanBuyRequest(BaseModel):
    book_name: str
    user_budget: float = Field(ge=0)
    actual_price_with_promo: float = Field(ge=0, le=1)


app = FastAPI()

book_prices = {
    "Граф Монте-Кристо": 1000
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello_user(user_name: str = Query(..., alias="user-name", regex="^[a-zA-Z]+$")):
    return {"message": "Hello World, {}!".format(user_name)}


@app.post("/book/can-buy")
async def is_user_can_buy(can_buy_request: CanBuyRequest, response: Response):
    if can_buy_request.book_name not in book_prices:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "That book does not exist"}
    else:
        actual_price = book_prices[can_buy_request.book_name] * can_buy_request.actual_price_with_promo
        if can_buy_request.user_budget >= actual_price:
            return {"message": "Can buy {} for {}".format(can_buy_request.book_name, actual_price)}
        else:
            return {"message": "Can not buy {}".format(can_buy_request.book_name)}
