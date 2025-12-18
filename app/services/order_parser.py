from app.ai.registry import AIModelRegistry
import json

ORDER_PARSER_PROMPT = """
Extrae productos y cantidades del mensaje del cliente.

Responde SOLO en JSON con este formato:
{
  "items": [
    { "name": "<producto>", "quantity": <numero> }
  ]
}

Mensaje:
"{message}"
"""

async def parse_order(message: str) -> list[dict]:
    model = AIModelRegistry.get("openai-gpt")

    result = await model.instance.generate(
        ORDER_PARSER_PROMPT.format(message=message),
        temperature=0.0,
        max_tokens=100
    )

    try:
        data = json.loads(result["text"])
        return data.get("items", [])
    except Exception:
        return []
