from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API de gestion de tâches — DevOps Fil Rouge B3",
    version="1.0.0",
)

app.include_router(tasks.router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
