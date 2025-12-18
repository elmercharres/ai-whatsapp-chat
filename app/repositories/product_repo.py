"""
Repository for Product data access operations.
"""
from sqlalchemy.orm import Session
from app.models.product import Product
from typing import Optional, List


class ProductRepository:
    """Repository class for Product operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Get product by ID."""
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def get_by_sku(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        return self.db.query(Product).filter(Product.sku == sku).first()
    
    def get_by_tenant(self, tenant_id: int, skip: int = 0, limit: int = 100) -> List[Product]:
        """Get all products for a tenant with pagination."""
        return self.db.query(Product).filter(
            Product.tenant_id == tenant_id
        ).offset(skip).limit(limit).all()
    
    def get_available_products(self, tenant_id: int) -> List[Product]:
        """Get all available products for a tenant."""
        return self.db.query(Product).filter(
            Product.tenant_id == tenant_id,
            Product.is_available == True,
            Product.stock_quantity > 0
        ).all()
    
    def search_by_name(self, tenant_id: int, name: str) -> List[Product]:
        """Search products by name for a tenant."""
        return self.db.query(Product).filter(
            Product.tenant_id == tenant_id,
            Product.name.ilike(f"%{name}%")
        ).all()
    
    def create(self, product: Product) -> Product:
        """Create a new product."""
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def update(self, product: Product) -> Product:
        """Update an existing product."""
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def delete(self, product_id: int) -> bool:
        """Delete a product by ID."""
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False
    
    def update_stock(self, product_id: int, quantity: int) -> Optional[Product]:
        """Update product stock quantity."""
        product = self.get_by_id(product_id)
        if product:
            product.stock_quantity = quantity
            return self.update(product)
        return None
