import os
import re
import PyPDF2
import chromadb
from chromadb.config import Settings
from openai import OpenAI

# ================================
# CONFIGURATION
# ================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment variables")

SDS_FOLDER = "./sds_pdf"
CHROMA_PATH = "./chroma_data"
COLLECTION_NAME = "sds_collection"
EMBED_MODEL = "text-embedding-3-large"

client = OpenAI(api_key=OPENAI_API_KEY)

# ================================
# HELPER FUNCTIONS
# ================================

def extract_text_from_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


SECTION_HEADER_RE = r"(?m)^\s*(\d{1,2})\.\s+([A-Za-z].+?)$"


def split_into_sections(text):
    sections = []
    matches = list(re.finditer(SECTION_HEADER_RE, text))

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        sections.append({
            "section_number": m.group(1).strip(),
            "section_title": m.group(2).strip(),
            "section_text": text[start:end].strip(),
        })

    return sections


def get_embedding(text):
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return resp.data[0].embedding


# ================================
# MAIN INGEST FUNCTION
# ================================

def ingest_into_chroma():
    print("\n📦 Initializing ChromaDB...")
    chroma_client = chromadb.PersistentClient(
        path=CHROMA_PATH,
        settings=Settings(anonymized_telemetry=False)
    )

    try:
        collection = chroma_client.get_collection(COLLECTION_NAME)
        print("ℹ️ Collection found.")
    except:
        print("➕ Creating new collection:", COLLECTION_NAME)
        collection = chroma_client.create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )

    print("\n📂 Scanning SDS folder:", SDS_FOLDER)

    for file in os.listdir(SDS_FOLDER):
        if not file.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(SDS_FOLDER, file)
        print(f"\n📄 Processing: {file}")

        raw_text = extract_text_from_pdf(pdf_path)
        sections = split_into_sections(raw_text)

        if not sections:
            print("⚠️ No SDS sections detected!")
            continue

        for sec in sections:
            section_id = f"{file}_sec_{sec['section_number']}"

            embedding = get_embedding(sec["section_text"])

            collection.add(
                ids=[section_id],
                embeddings=[embedding],
                documents=[sec["section_text"]],
                metadatas=[{
                    "file": file,
                    "section": sec["section_number"],
                    "title": sec["section_title"],
                }]
            )

        print(f"✅ Ingested {len(sections)} sections from {file}")

    print("\n🎉 DONE! SDS documents ingested into Chroma.")


if __name__ == "__main__":
    ingest_into_chroma()
