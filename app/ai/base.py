from abc import ABC, abstractmethod

class AIResponse:
    def __init__(self, text: str, usage: dict | None = None):
        self.text = text
        self.usage = usage or {}

class AIAdapter(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.7,
        max_tokens: int = 512
    ) -> AIResponse:
        pass
