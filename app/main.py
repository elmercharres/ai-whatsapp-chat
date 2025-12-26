from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api import chat, campaigns, orders, admin

setup_logging()

app = FastAPI(
    title="AI Chat SaaS",
    version="1.0.0"
)

app.include_router(chat.router, prefix="/api/chat")
app.include_router(campaigns.router, prefix="/api/campaigns")
app.include_router(orders.router, prefix="/api/orders")
app.include_router(admin.router, prefix="/api/admin")
