from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Member Registry API",
    description="A standalone Member Registry API Service with CRUD operations",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
