import strawberry
from typing import Optional, List
from sqlalchemy.orm import Session
from .types import ItemType 
from .resolvers import get_item, list_items

@strawberry.type
class Query:
    @strawberry.field
    def get_item(info, item_id: int) -> Optional[ItemType]:
        print(info.context["db"])
        db: Session = info.context["db"]
        db_item = get_item(db, item_id)
        if db_item:
            return ItemType(
                id=db_item.id,
                name=db_item.name,
                price=db_item.price,
                is_offer=db_item.is_offer
            )
        return None

    @strawberry.field
    def list_items(self, info) -> List[ItemType]:
        db: Session = info.context["db"]
        db_items = list_items(db)
        return [
            ItemType(
                id=item.id,
                name=item.name,
                price=item.price,
                is_offer=item.is_offer
            )
            for item in db_items
        ]
