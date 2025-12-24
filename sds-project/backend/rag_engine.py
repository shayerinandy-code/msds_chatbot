import chromadb

# Persistent Chroma client
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_db"
    )
)

collection = client.get_or_create_collection(
    name="sds_collection"
)

def get_sds_answer(query: str, product: str):
    """
    Returns EXACT SDS TEXT — NO MODIFICATION
    """

    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={"product": product}
    )

    if not results or not results.get("documents"):
        return None, 0

    # TAKE TOP MATCH — EXACT RAW TEXT
    exact_text = results["documents"][0][0]

    return exact_text, 9
