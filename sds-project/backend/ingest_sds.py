import os
from PyPDF2 import PdfReader
import chromadb
from chromadb.utils import embedding_functions

PDF_DIR = "sds_pdf"
CHROMA_DIR = "chroma"
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

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text, chunk_size=800):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def ingest_all_pdfs():
    total = 0
    for file in os.listdir(PDF_DIR):
        if not file.lower().endswith(".pdf"):
            continue

        product = os.path.splitext(file)[0]
        text = extract_text(os.path.join(PDF_DIR, file))

        for i, chunk in enumerate(chunk_text(text)):
            collection.add(
                documents=[chunk],
                metadatas=[{"product": product}],
                ids=[f"{product}_{i}"]
            )
            total += 1

        print(f"✅ Ingested: {product}")

    print(f"\n🎉 Total chunks added: {total}")

if __name__ == "__main__":
    ingest_all_pdfs()
