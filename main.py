from fastapi import FastAPI
from pydantic import BaseModel
from agent import simple_agent
app = FastAPI()
class Question(BaseModel):
    question: str
@app.get("/")
def home():
    return {"message": "Agentic backend running! Go to /docs to test"}
@app.post("/ask")
def ask(q: Question):
    answer = simple_agent(q.question)
    return {"question": q.question, "answer": answer}
