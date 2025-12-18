"""
Data repositories
"""
from app.repositories.tenant_repo import TenantRepository
from app.repositories.product_repo import ProductRepository
from app.repositories.order_repo import OrderRepository

__all__ = ["TenantRepository", "ProductRepository", "OrderRepository"]
