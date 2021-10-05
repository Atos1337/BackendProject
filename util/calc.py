from typing import Optional


def calc_actual_book_price_for_user(
        book_price: Optional[float],
        book_promo: Optional[float],
        user_promo: Optional[float]
):
    if not book_price:
        return None
    if not user_promo and not book_promo:
        return book_price
    elif not (user_promo and book_promo):
        return book_price * (user_promo or book_promo)
    else:
        return book_price * min(user_promo, book_promo)
