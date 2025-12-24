from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

PERSIST_DIR = "./chroma"

db = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=OpenAIEmbeddings()
)

print("Total documents:", db._collection.count())
