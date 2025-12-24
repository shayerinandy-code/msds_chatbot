import chromadb
from chromadb.utils import embedding_functions

CHROMA_DIR = "chroma"          # ✅ MUST match ingest_sds.py & api.py
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

count = collection.count()
print(f"Total documents: {count}")
