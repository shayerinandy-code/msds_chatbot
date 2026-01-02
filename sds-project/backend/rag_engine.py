from query_sds import query_sds
from confidence import calculate_confidence


def answer_question(question: str):
    """
    Answers SDS questions using ONLY text retrieved from ChromaDB.
    NO summarization. NO paraphrasing. Compliance-safe.
    """

    # 1️⃣ Retrieve documents from ChromaDB
    documents, metadatas = query_sds(question, n_results=5)

    if not documents:
        return {
            "answer": "Not found in SDS.",
            "confidence": 5.0,
            "source": "",
            "highlighted_text": ""
        }

    # 2️⃣ Pick the most relevant chunk (top result)
    best_text = documents[0].strip()
    best_meta = metadatas[0]

    if not best_text:
        return {
            "answer": "Not found in SDS.",
            "confidence": 5.0,
            "source": "",
            "highlighted_text": ""
        }

    # 3️⃣ Calculate confidence (STRICT SDS MODE)
    confidence = calculate_confidence(
        question=question,
        answer=best_text,
        mode="strict"
    )

    # 4️⃣ Build source string
    source = f"{best_meta.get('source')} (Page {best_meta.get('page')})"

    # 5️⃣ FINAL RESPONSE (EXACT TEXT FROM PDF)
    return {
        "answer": best_text,
        "confidence": confidence,
        "source": source,
        "highlighted_text": best_text
    }
