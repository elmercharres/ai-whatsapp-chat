from app.ai.registry import AIModelRegistry

INTENT_PROMPT = """
Clasifica el mensaje del usuario en UNA sola intención.

Intenciones posibles:
- greeting
- catalog
- product_query
- order
- human
- unknown

Responde SOLO en JSON con esta forma:
{
  "intent": "<intent>"
}

Mensaje del usuario:
"{message}"
"""

async def detect_intent(message: str) -> str:
    model = AIModelRegistry.get("openai-gpt")

    prompt = INTENT_PROMPT.format(message=message)

    result = await model.instance.generate(
        prompt,
        temperature=0.0,
        max_tokens=50
    )

    try:
        import json
        data = json.loads(result["text"])
        return data.get("intent", "unknown")
    except Exception:
        return "unknown"
