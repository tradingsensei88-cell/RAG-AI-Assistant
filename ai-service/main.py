from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from process_incoming_Q import process_incoming_Q

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Query):
    answer = process_incoming_Q(data.question)
    return {"response": answer}

#to start https://chatgpt.com/share/69ada5e7-f59c-8006-aca7-4e5d84993440