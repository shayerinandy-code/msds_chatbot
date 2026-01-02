# load_sds_pdf.py
import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

PDF_FOLDER = "sds_pdf"

def load_and_split_pdfs(pdf_folder=PDF_FOLDER):
    documents = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    for file in os.listdir(pdf_folder):
        if not file.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(pdf_folder, file)
        reader = PdfReader(file_path)

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if not text:
                continue

            chunks = splitter.split_text(text)

            for chunk in chunks:
                documents.append(
                    Document(
                        page_content=chunk.strip(),
                        metadata={
                            "source": file,
                            "page": page_number
                        }
                    )
                )

    print(f"📄 Chunks created: {len(documents)}")
    return documents
