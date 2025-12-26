"""
WhatsApp webhook API endpoints.
"""
from fastapi import APIRouter, Form
from app.services.whatsapp_service import handle_whatsapp_message
from app.schemas.whatsapp import WhatsAppMessage

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(msg: WhatsAppMessage):
    return await handle_whatsapp_message(
        from_number=msg.From,
        message=msg.Body
    )