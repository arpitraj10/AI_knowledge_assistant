import requests
import os

ENDEE_API_KEY = os.getenv("ENDEE_API_KEY")
ENDEE_BASE_URL = os.getenv("ENDEE_BASE_URL")
ENDEE_INDEX = os.getenv("ENDEE_INDEX_NAME")

HEADERS = {
    "Authorization": f"Bearer {ENDEE_API_KEY}",
    "Content-Type": "application/json"
}

def upsert_vectors(vectors):
    """
    vectors = [
      {
        "id": "doc_1",
        "values": [0.123, 0.456, ...],
        "metadata": {"text": "chunk text"}
      }
    ]
    """
    url = f"{ENDEE_BASE_URL}/v1/indexes/{ENDEE_INDEX}/vectors"
    response = requests.post(url, headers=HEADERS, json={"vectors": vectors})
    response.raise_for_status()
    return response.json()

def query_vectors(query_vector, top_k=3):
    url = f"{ENDEE_BASE_URL}/v1/indexes/{ENDEE_INDEX}/query"
    payload = {
        "vector": query_vector,
        "top_k": top_k,
        "include_metadata": True
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()
