"""
Repository for Order data access operations.
"""
from sqlalchemy.orm import Session
from app.models.order import Order, OrderStatus
from typing import Optional, List


class OrderRepository:
    """Repository class for Order operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, order_id: int) -> Optional[Order]:
        """Get order by ID."""
        return self.db.query(Order).filter(Order.id == order_id).first()
    
    def get_by_tenant(self, tenant_id: int, skip: int = 0, limit: int = 100) -> List[Order]:
        """Get all orders for a tenant with pagination."""
        return self.db.query(Order).filter(
            Order.tenant_id == tenant_id
        ).order_by(Order.created_at.desc()).offset(skip).limit(limit).all()
    
    def get_by_customer(self, tenant_id: int, customer_phone: str) -> List[Order]:
        """Get all orders for a specific customer."""
        return self.db.query(Order).filter(
            Order.tenant_id == tenant_id,
            Order.customer_phone == customer_phone
        ).order_by(Order.created_at.desc()).all()
    
    def get_by_status(self, tenant_id: int, status: OrderStatus) -> List[Order]:
        """Get all orders with a specific status."""
        return self.db.query(Order).filter(
            Order.tenant_id == tenant_id,
            Order.status == status
        ).order_by(Order.created_at.desc()).all()
    
    def get_recent_order(self, tenant_id: int, customer_phone: str) -> Optional[Order]:
        """Get the most recent order for a customer."""
        return self.db.query(Order).filter(
            Order.tenant_id == tenant_id,
            Order.customer_phone == customer_phone
        ).order_by(Order.created_at.desc()).first()
    
    def create(self, order: Order) -> Order:
        """Create a new order."""
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order
    
    def update(self, order: Order) -> Order:
        """Update an existing order."""
        self.db.commit()
        self.db.refresh(order)
        return order
    
    def update_status(self, order_id: int, status: OrderStatus) -> Optional[Order]:
        """Update order status."""
        order = self.get_by_id(order_id)
        if order:
            order.status = status
            return self.update(order)
        return None
    
    def delete(self, order_id: int) -> bool:
        """Delete an order by ID."""
        order = self.get_by_id(order_id)
        if order:
            self.db.delete(order)
            self.db.commit()
            return True
        return False
