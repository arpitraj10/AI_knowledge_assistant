from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from endee_client import query_vectors

def generate_answer(query):
    embeddings = OpenAIEmbeddings()
    query_vector = embeddings.embed_query(query)

    results = query_vectors(query_vector, top_k=3)

    context_chunks = [
        match["metadata"]["text"]
        for match in results["matches"]
    ]

    context = "\n\n".join(context_chunks)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = f"""
You are an AI Knowledge Assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content
