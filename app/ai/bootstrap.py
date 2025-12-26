from app.ai.registry import AIModelRegistry, AIModelConfig
from app.ai.providers.openai_provider import OpenAIProvider
from app.ai.providers.claude_provider import ClaudeProvider
from app.core.config import settings

AIModelRegistry.register(
    AIModelConfig(
        name="openai-gpt",
        provider="openai",
        cost_tier="medium",
        max_context=128000,
        supports_tools=True,
        instance=OpenAIProvider(
            api_key=settings.openai_api_key,
            model="gpt-4o-mini"
        )
    )
)

AIModelRegistry.register(
    AIModelConfig(
        name="claude-sonnet-4-5",
        provider="anthropic",
        cost_tier="low",
        max_context=200000,
        supports_tools=False,
        instance=ClaudeProvider(
            api_key=settings.anthropic_api_key,
            model="claude-sonnet-4-5"
        )
    )
)
