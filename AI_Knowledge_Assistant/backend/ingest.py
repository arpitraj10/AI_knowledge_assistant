import uuid
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from endee_client import upsert_vectors

def load_documents(path="data/documents/sample_docs.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def ingest():
    text = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    vectors = []

    for chunk in chunks:
        vector = embeddings.embed_query(chunk)
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {"text": chunk}
        })

    upsert_vectors(vectors)
    print("✅ Documents successfully ingested into Endee")

if __name__ == "__main__":
    ingest()
