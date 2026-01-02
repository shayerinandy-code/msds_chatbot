# check_chroma.py

import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collections = client.list_collections()

print("Available collections:")
for c in collections:
    print("-", c.name)
