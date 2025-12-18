def build_prompt(
    *,
    tenant_name,
    business_type,
    catalog,
    memory,
    user_message
):
    history = "\n".join(
        f"{m['role']}: {m['content']}"
        for m in memory
    )

    return f"""
Eres un asistente de ventas de {tenant_name}.
Tipo de negocio: {business_type}

Historial reciente:
{history}

Catálogo:
{catalog}

Usuario:
{user_message}
"""
