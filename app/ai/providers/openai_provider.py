from openai import AsyncOpenAI
from app.ai.base import AIProvider

class OpenAIProvider(AIProvider):

    def __init__(self, api_key: str, model: str):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, *, temperature=0.7, max_tokens=512, context=None):
        response = await self.client.responses.create(
            model=self.model,
            input=prompt,
            max_output_tokens=max_tokens,
            temperature=temperature
        )

        text = response.output_text

        usage = response.usage or {}

        return {
            "text": text,
            "usage": {
                "input_tokens": getattr(usage, "input_tokens", None),
                "output_tokens": getattr(usage, "output_tokens", None)
            },
            "model": self.model
        }
