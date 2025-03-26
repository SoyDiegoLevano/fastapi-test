import strawberry
from typing import Optional

@strawberry.type
class ItemType:
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None
