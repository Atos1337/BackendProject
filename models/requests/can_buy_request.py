from pydantic import BaseModel, Field


class CanBuyRequest(BaseModel):
    book_name: str
    user_budget: float = Field(ge=0)
    actual_price_with_promo: float = Field(ge=0, le=1)
