from fastapi import FastAPI

app = FastAPI(
    title="NovaChem-AI",
    description="AI-powered Chemistry Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "NovaChem-AI",
        "status": "Running",
        "message": "Welcome to NovaChem-AI"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
