from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_engine import answer_question

app = FastAPI()

# ✅ CORS FIX (THIS IS THE MOST IMPORTANT PART)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_sds_api(req: QueryRequest):
    result = answer_question(req.question)
    return result
