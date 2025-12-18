from app.services.audience_service import get_audience
from app.services.whatsapp_service import WhatsAppService

async def run_campaign(
    *,
    db,
    tenant_id: str,
    campaign,
    segment: str,
    whatsapp_service: WhatsAppService
):
    audience = get_audience(db, tenant_id, segment)

    for (phone,) in audience:
        await whatsapp_service.send_message(
            to=phone,
            text=campaign.message
        )

    campaign.status = "sent"
    db.commit()
