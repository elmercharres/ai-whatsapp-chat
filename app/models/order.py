"""
Order model for managing customer orders.
Each order belongs to a tenant and contains order items.
"""
from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import uuid

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"))
    whatsapp_user: Mapped[str] = mapped_column(String)
    items: Mapped[dict] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(String, default="pending")
