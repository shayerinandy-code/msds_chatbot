from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

db = Chroma(
    persist_directory="./chroma",
    embedding_function=OpenAIEmbeddings()
)

docs = db.similarity_search("first aid", k=5)

for d in docs:
    print(d.metadata)
