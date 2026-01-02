# ingest_sds.py
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from load_sds_pdf import load_and_split_pdfs

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "sds_documents"

def ingest_pdfs():
    print("📥 Loading and splitting PDFs...")
    docs = load_and_split_pdfs()

    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    texts = [d.page_content for d in docs]
    metadatas = [d.metadata for d in docs]
    ids = [f"doc_{i}" for i in range(len(docs))]

    print("📦 Storing embeddings in ChromaDB...")
    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

    print("✅ Ingestion completed successfully!")
    print(f"📚 Collection name: {COLLECTION_NAME}")

if __name__ == "__main__":
    ingest_pdfs()
