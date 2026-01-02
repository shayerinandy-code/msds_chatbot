# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import answer_question

app = FastAPI(title="SDS Query API")

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    confidence: float
    source: str

@app.post("/query", response_model=QueryResponse)
def query_sds_api(req: QueryRequest):
    result = answer_question(req.question)

    if result is None:
        return {
            "answer": "No exact answer found in SDS documents.",
            "confidence": 0.0,
            "source": "N/A"
        }

    # result is already formatted text → parse it
    lines = result.splitlines()

    answer = []
    confidence = 0.0
    source = ""

    for line in lines:
        if line.startswith("Confidence:"):
            confidence = float(line.replace("Confidence:", "").strip())
        elif line.startswith("Source:"):
            source = line.replace("Source:", "").strip()
        else:
            answer.append(line)

    return {
        "answer": "\n".join(answer).strip(),
        "confidence": confidence,
        "source": source
    }
