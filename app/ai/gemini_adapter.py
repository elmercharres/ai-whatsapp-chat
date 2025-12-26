import google.generativeai as genai
from app.ai.base import AIAdapter, AIResponse
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class GeminiAdapter(AIAdapter):
    """
    Adapter para Google Gemini
    Compatible con gemini-1.5-pro, gemini-1.5-flash
    """

    def __init__(self, model: str):
        self.model = model

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.client = genai.GenerativeModel(
            model_name=self.model
        )

    async def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.7,
        max_tokens: int = 512
    ) -> AIResponse:
        try:
            response = await self.client.generate_content_async(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens
                }
            )

            text = response.text or ""

            usage = {
                "input_tokens": getattr(response.usage_metadata, "prompt_token_count", None),
                "output_tokens": getattr(response.usage_metadata, "candidates_token_count", None),
                "total_tokens": getattr(response.usage_metadata, "total_token_count", None),
            }

            logger.info(
                "Gemini response generated",
                extra={
                    "model": self.model,
                    "tokens": usage
                }
            )

            return AIResponse(text=text, usage=usage)

        except Exception as e:
            logger.exception(
                "GeminiAdapter failed",
                extra={"model": self.model}
            )
            raise
