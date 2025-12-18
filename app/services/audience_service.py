from app.models.conversation import Conversation
from app.models.order import Order

def get_audience(db, tenant_id: str, segment: str):
    if segment == "all":
        return (
            db.query(Conversation.whatsapp_user)
            .filter_by(tenant_id=tenant_id)
            .distinct()
            .all()
        )

    if segment == "buyers":
        return (
            db.query(Order.whatsapp_user)
            .filter_by(tenant_id=tenant_id)
            .distinct()
            .all()
        )

    return []
