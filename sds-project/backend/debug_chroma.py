import os
import chromadb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=CHROMA_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection("sds_collection")

data = collection.get()
print("Total documents:", len(data["ids"]))
