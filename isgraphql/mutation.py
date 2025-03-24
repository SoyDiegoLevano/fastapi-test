import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from .types import ItemType
from .resolvers import create_item_resolver, update_item_resolver, delete_item_resolver
 
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, info, name: str, price: float, is_offer: Optional[bool] = False) -> ItemType:
        db: Session = info.context["db"]
        new_item = create_item_resolver(db, name, price, is_offer)
        return ItemType(
            id=new_item.id,
            name=new_item.name,
            price=new_item.price,
            is_offer=new_item.is_offer
        )

    @strawberry.mutation
    def update_item(self, info, item_id: int, name: str, price: float, is_offer: Optional[bool] = False) -> Optional[ItemType]:
        db: Session = info.context["db"]
        updated_item = update_item_resolver(db, item_id, name, price, is_offer)
        if updated_item:
            return ItemType(
                id=updated_item.id,
                name=updated_item.name,
                price=updated_item.price,
                is_offer=updated_item.is_offer
            )
        return None

    @strawberry.mutation
    def delete_item(self, info, item_id: int) -> bool:
        db: Session = info.context["db"]
        return delete_item_resolver(db, item_id)
