from app.ai.registry import MODEL_REGISTRY
from app.ai.router import select_model
from app.services.intent_service import detect_intent

async def generate_ai_response(prompt: str) -> str:
    intent = detect_intent(prompt)
    model_name = select_model(intent)
    model = MODEL_REGISTRY[model_name]

    response = await model.generate(prompt)
    return response.text
