from abc import ABC, abstractmethod
from typing import Dict, Any

class AIProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.7,
        max_tokens: int = 512,
        context: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:
        """
        Returns:
        {
          "text": str,
          "usage": {
            "input_tokens": int,
            "output_tokens": int
          },
          "model": str
        }
        """
        pass
