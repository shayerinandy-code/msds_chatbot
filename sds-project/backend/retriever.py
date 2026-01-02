import chromadb
from chromadb.config import Settings
from config import CHROMA_DB_DIR

client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DB_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(name="sds_docs")


def retrieve_chunks(query: str, k: int = 8):
    result = collection.query(
        query_texts=[query],
        n_results=k
    )

    if not result or not result.get("documents"):
        return []

    documents = result["documents"][0]
    return documents
