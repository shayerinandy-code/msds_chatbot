import os

# Base directory (backend folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# PDF folder name (DO NOT CHANGE the folder name)
PDF_FOLDER = os.path.join(BASE_DIR, "sds_pdf")

# Chroma DB directory
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")

# Chroma collection name
COLLECTION_NAME = "sds_documents"
