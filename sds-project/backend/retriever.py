# retriever.py

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

PERSIST_DIR = "./chroma"

def retrieve_sds(query: str, product: str):
    db = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=OpenAIEmbeddings()
    )

    docs = db.similarity_search(
        query,
        k=5,
        filter={"product": product}
    )

    return docs
