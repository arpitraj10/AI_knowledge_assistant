from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import generate_answer

app = FastAPI(title="AI Knowledge Assistant")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(request: QueryRequest):
    answer = generate_answer(request.question)
    return {"answer": answer}
