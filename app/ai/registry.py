from app.ai.openai_adapter import OpenAIAdapter
from app.ai.claude_adapter import ClaudeAdapter
from app.ai.gemini_adapter import GeminiAdapter

MODEL_REGISTRY = {
    "gpt-4o-mini": OpenAIAdapter("gpt-4o-mini"),
    "claude-sonnet-4-5": ClaudeAdapter("claude-sonnet-4-5"),
    "gemini-1.5-pro": GeminiAdapter("gemini-1.5-pro"),
}
