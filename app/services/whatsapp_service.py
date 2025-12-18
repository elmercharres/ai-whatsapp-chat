class WhatsAppService:

    def __init__(self, provider):
        self.provider = provider

    async def send_message(self, to: str, text: str):
        await self.provider.send_text(
            to=to,
            text=text
        )
