HANDOFF_KEYWORDS = [
    "hablar con alguien",
    "asesor",
    "persona",
    "humano",
    "llamar",
    "contactar"
]

def wants_human(message: str) -> bool:
    msg = message.lower()
    return any(k in msg for k in HANDOFF_KEYWORDS)
