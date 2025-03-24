from sqlalchemy.orm import Session
from database import ItemDB
 
def get_item(db: Session, item_id: int):
    return db.query(ItemDB).filter(ItemDB.id == item_id).first()

def list_items(db: Session):
    return db.query(ItemDB).all()

def create_item_resolver(db: Session, name: str, price: float, is_offer: bool):
    new_item = ItemDB(name=name, price=price, is_offer=is_offer)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item_resolver(db: Session, item_id: int, name: str, price: float, is_offer: bool):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if item:
        item.name = name
        item.price = price
        item.is_offer = is_offer
        db.commit()
        db.refresh(item)
    return item

def delete_item_resolver(db: Session, item_id: int):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False
