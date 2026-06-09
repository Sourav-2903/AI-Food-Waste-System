from fastapi import FastAPI

app = FastAPI(
    title="AI Food Waste System"
)

@app.get("/")
def home():
    return {
        "message":
        "Welcome to AI Food Waste System"
    }

@app.get("/health")
def health():
    return {
        "status":"running"
    }