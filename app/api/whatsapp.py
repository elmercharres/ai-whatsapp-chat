"""
WhatsApp webhook API endpoints.
"""
from fastapi import APIRouter, Form
from app.services.whatsapp_service import handle_whatsapp_message

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...)
):
    return await handle_whatsapp_message(
        from_number=From,
        message=Body
    )
