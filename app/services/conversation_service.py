from app.models.conversation import Conversation
from sqlalchemy.orm import Session

MAX_MEMORY = 6  # últimos 6 mensajes

def get_or_create_conversation(
    db: Session,
    tenant_id: str,
    whatsapp_user: str
) -> Conversation:

    convo = (
        db.query(Conversation)
        .filter_by(
            tenant_id=tenant_id,
            whatsapp_user=whatsapp_user
        )
        .first()
    )

    if not convo:
        convo = Conversation(
            tenant_id=tenant_id,
            whatsapp_user=whatsapp_user,
            memory=[]
        )
        db.add(convo)
        db.commit()
        db.refresh(convo)

    return convo


def append_memory(convo: Conversation, role: str, content: str):
    convo.memory.append({
        "role": role,
        "content": content
    })

    convo.memory = convo.memory[-MAX_MEMORY:]
