# query_sds.py
import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "sds_documents"

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def query_sds(query: str, n_results: int = 5):
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # 🔒 ONLY RETURN WHAT RAG EXPECTS
    return documents, metadatas
