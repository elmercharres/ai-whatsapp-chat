from app.ai.base import AIProvider

class GeminiProvider(AIProvider):
    async def generate(self, prompt: str, *, temperature=0.7, max_tokens=512, context=None):
        raise NotImplementedError("Gemini not enabled yet")
