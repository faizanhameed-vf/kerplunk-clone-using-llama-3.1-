from fastapi import FastAPI
from pydantic import BaseModel
import ollama

# Initialize FastAPI app
app = FastAPI()

# Define request body model
class Prompt(BaseModel):
    prompt: str

# POST endpoint to interact with Llama 3.1
@app.post("/llama-chat/")
async def llama_chat(request: Prompt):
    try:
        # Interact with Llama 3.1 model using Ollama
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": request.prompt}])
        return {"response": response['message']['content']}
    except Exception as e:
        return {"error": str(e)}

@app.post("/llama-chat-questions/")
async def llama_chat_questions(request: Prompt):
    try:
        # Interact with Llama 3.1 model using Ollama
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": request.prompt}])
        return {"response": response['message']['content']}
    except Exception as e:
        return {"error": str(e)}

@app.post("/llama-chat-review/")
async def llama_chat_questions(request: Prompt):
    try:
        # Interact with Llama 3.1 model using Ollama
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": request.prompt}])
        return {"response": response['message']['content']}
    except Exception as e:
        return {"error": str(e)}



# Root endpoint
@app.get("/")
async def root():
    return {"message": "Llama 3.1 FastAPI is running!"}
