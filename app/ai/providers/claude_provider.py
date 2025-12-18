from anthropic import AsyncAnthropic
from app.ai.base import AIProvider

class ClaudeProvider(AIProvider):

    def __init__(self, api_key: str, model: str):
        self.client = AsyncAnthropic(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, *, temperature=0.7, max_tokens=512, context=None):
        message = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )

        text = message.content[0].text if message.content else ""
        usage = message.usage or {}

        return {
            "text": text,
            "usage": {
                "input_tokens": getattr(usage, "input_tokens", None),
                "output_tokens": getattr(usage, "output_tokens", None)
            },
            "model": self.model
        }
