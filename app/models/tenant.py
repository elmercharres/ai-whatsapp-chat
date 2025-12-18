"""
Tenant model for multi-tenant support.
Each tenant represents a business/organization using the WhatsApp chat service.
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import uuid


class Tenant(Base):
    __tablename__ = "tenants"
    
    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String)
    whatsapp_number: Mapped[str] = mapped_column(String, unique=True)
    business_type: Mapped[str] = mapped_column(String)  # ecommerce | restaurant
