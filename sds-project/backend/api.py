from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI()

CHROMA_DIR = "chroma"   # ✅ SAME FOLDER
COLLECTION_NAME = "sds_collection"

embedding_function = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=CHROMA_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)

class QueryRequest(BaseModel):
    query: str
    product: str | None = None

@app.post("/api/v1/query")
def query_sds(req: QueryRequest):
    results = collection.query(
        query_texts=[req.query],
        n_results=5
    )

    if not results["documents"] or not results["documents"][0]:
        return {"answer": "No relevant information found in SDS documents."}

    answer = "\n\n".join(results["documents"][0])
    return {"answer": answer}
