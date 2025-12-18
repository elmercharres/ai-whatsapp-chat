from dataclasses import dataclass
from typing import Dict
from app.ai.base import AIProvider

@dataclass
class AIModelConfig:
    name: str
    provider: str
    cost_tier: str        # low | medium | high
    max_context: int
    supports_tools: bool
    instance: AIProvider


class AIModelRegistry:
    _models: Dict[str, AIModelConfig] = {}

    @classmethod
    def register(cls, config: AIModelConfig):
        cls._models[config.name] = config

    @classmethod
    def get(cls, model_name: str) -> AIModelConfig:
        if model_name not in cls._models:
            raise ValueError(f"Model '{model_name}' not registered")
        return cls._models[model_name]

    @classmethod
    def all(cls):
        return cls._models
