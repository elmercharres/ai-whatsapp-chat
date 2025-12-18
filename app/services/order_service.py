"""
Order service for managing order business logic.
"""

from sqlalchemy.orm import Session
from app.models.order import Order

def create_order(
    db: Session,
    tenant_id: str,
    whatsapp_user: str,
    items: list[dict]
) -> Order:
    order = Order(
        tenant_id=tenant_id,
        whatsapp_user=whatsapp_user,
        items=items
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
