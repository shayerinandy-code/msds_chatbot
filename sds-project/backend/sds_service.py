from rag_engine import retrieve_exact_sds_text, explain_sds

def process_sds_query(query: str, product: str):
    sds_text, confidence = retrieve_exact_sds_text(
        query=query,
        product=product
    )

    if not sds_text or confidence < 7:
        return {
            "answer": None,
            "confidence": confidence,
            "action": "ESCALATE"
        }

    # ✅ OPTIONAL explanation mode (ChatGPT-like, but safe)
    if any(word in query.lower() for word in ["explain", "simple", "summarize"]):
        explained_text = explain_sds(sds_text, query)
        return {
            "answer": explained_text,
            "confidence": confidence,
            "action": "RESPOND"
        }

    # 🔒 Default: exact SDS text (compliance-safe)
    return {
        "answer": sds_text,
        "confidence": confidence,
        "action": "RESPOND"
    }
