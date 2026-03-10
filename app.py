import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from rag import RagEngine

app = FastAPI()

rag = RagEngine()

os.makedirs("uploads", exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():

    return {"msg":"RagDB running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    path = f"uploads/{file.filename}"

    with open(path,"wb") as buffer:

        shutil.copyfileobj(file.file,buffer)

    chunks = rag.add_document(path,file.filename)

    return {"message":"indexed","chunks":chunks}


@app.post("/ask")
async def ask(query:str = Form(...)):

    results = rag.search(query)

    answer = ""

    for r in results:

        answer += r["text"][:200] + "...\n\n"

    return {
        "answer":answer,
        "sources":results
    }
