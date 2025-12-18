from app.ai.registry import AIModelRegistry

class ModelRouter:

    @staticmethod
    def select(
        *,
        intent: str,
        prompt_length: int,
        multimodal: bool = False
    ) -> str:
        # Reglas simples (se vuelven complejas después)
        if multimodal:
            return "gemini-3-pro"

        if prompt_length > 2000:
            return "claude-sonnet-4-5"

        if intent in ("order", "action"):
            return "openai-gpt"

        return "openai-gpt"
