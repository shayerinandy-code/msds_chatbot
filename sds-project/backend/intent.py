# intent.py

def infer_section(question: str) -> str | None:
    q = question.lower()

    if "first aid" in q:
        return "first aid"
    if "fire" in q or "flammable" in q:
        return "fire"
    if "storage" in q or "handling" in q:
        return "storage"
    if "exposure" in q or "ppe" in q:
        return "exposure"
    if "spill" in q or "leak" in q:
        return "spill"

    return None
