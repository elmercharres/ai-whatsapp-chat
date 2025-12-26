from anthropic import AsyncAnthropic
from app.ai.base import AIAdapter, AIResponse
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class ClaudeAdapter(AIAdapter):
    """
    Adapter para modelos Claude (Anthropic)
    Compatible con claude-sonnet-4-5, haiku-4-5, opus-4-5
    """

    def __init__(self, model: str):
        self.model = model
        self.client = AsyncAnthropic(
            api_key=settings.CLAUDE_API_KEY
        )

    async def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.7,
        max_tokens: int = 512
    ) -> AIResponse:
        try:
            message = await self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = message.content[0].text if message.content else ""

            usage = {
                "input_tokens": getattr(message.usage, "input_tokens", None),
                "output_tokens": getattr(message.usage, "output_tokens", None),
                "total_tokens": (
                    (message.usage.input_tokens or 0)
                    + (message.usage.output_tokens or 0)
                ) if message.usage else None
            }

            logger.info(
                "Claude response generated",
                extra={
                    "model": self.model,
                    "tokens": usage
                }
            )

            return AIResponse(text=text, usage=usage)

        except Exception as e:
            logger.exception(
                "ClaudeAdapter failed",
                extra={"model": self.model}
            )
            raise
