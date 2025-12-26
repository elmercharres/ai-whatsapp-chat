from openai import AsyncOpenAI
from app.ai.base import AIAdapter, AIResponse
from app.config import settings

class OpenAIAdapter(AIAdapter):

    def __init__(self, model: str):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = model

    async def generate(self, prompt: str, **kwargs) -> AIResponse:
        res = await self.client.responses.create(
            model=self.model,
            input=prompt,
            **kwargs
        )
        return AIResponse(
            text=res.output_text,
            usage=res.usage.model_dump() if res.usage else {}
        )
