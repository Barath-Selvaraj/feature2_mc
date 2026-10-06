from fastapi import FastAPI

app = FastAPI(
    title="Feature 2 Service"
)


@app.get("/")
def root():
    return {
        "feature": "feature2",
        "message": "Feature 2 is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }