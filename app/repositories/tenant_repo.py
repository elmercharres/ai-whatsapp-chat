"""
Repository for Tenant data access operations.
"""
from sqlalchemy.orm import Session
from app.models.tenant import Tenant
from typing import Optional, List


class TenantRepository:
    """Repository class for Tenant operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, tenant_id: int) -> Optional[Tenant]:
        """Get tenant by ID."""
        return self.db.query(Tenant).filter(Tenant.id == tenant_id).first()
    
    def get_by_whatsapp_number(self, whatsapp_number: str) -> Optional[Tenant]:
        """Get tenant by WhatsApp number."""
        return self.db.query(Tenant).filter(Tenant.whatsapp_number == whatsapp_number).first()
    
    def get_by_api_key(self, api_key: str) -> Optional[Tenant]:
        """Get tenant by API key."""
        return self.db.query(Tenant).filter(Tenant.api_key == api_key).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Tenant]:
        """Get all tenants with pagination."""
        return self.db.query(Tenant).offset(skip).limit(limit).all()
    
    def get_active_tenants(self) -> List[Tenant]:
        """Get all active tenants."""
        return self.db.query(Tenant).filter(Tenant.is_active == True).all()
    
    def create(self, tenant: Tenant) -> Tenant:
        """Create a new tenant."""
        self.db.add(tenant)
        self.db.commit()
        self.db.refresh(tenant)
        return tenant
    
    def update(self, tenant: Tenant) -> Tenant:
        """Update an existing tenant."""
        self.db.commit()
        self.db.refresh(tenant)
        return tenant
    
    def delete(self, tenant_id: int) -> bool:
        """Delete a tenant by ID."""
        tenant = self.get_by_id(tenant_id)
        if tenant:
            self.db.delete(tenant)
            self.db.commit()
            return True
        return False
