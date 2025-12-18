from app.services.conversation_service import (
    get_or_create_conversation,
    append_memory
)
from app.services.handoff_detector import wants_human

async def generate_ai_response(
    *,
    db,
    tenant,
    whatsapp_user,
    user_message,
    catalog
):
    convo = get_or_create_conversation(
        db, tenant["id"], whatsapp_user
    )

    # 🧑‍💼 HANDOFF
    if wants_human(user_message):
        convo.status = "human"
        db.commit()
        return (
            "👨‍💼 Te pondremos en contacto con un asesor humano.\n"
            "Por favor espera un momento."
        )

    # Si está en modo humano, no responder
    if convo.status == "human":
        return ""  # WhatsApp humano responde

    append_memory(convo, "user", user_message)

    prompt = build_prompt(
        tenant_name=tenant["name"],
        business_type=tenant["business_type"],
        catalog=catalog,
        memory=convo.memory,
        user_message=user_message
    )

    model_name = ModelRouter.select(...)
    model = AIModelRegistry.get(model_name)

    result = await model.instance.generate(prompt)

    append_memory(convo, "assistant", result["text"])
    db.commit()

    return result["text"]
