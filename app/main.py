from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API", version="1.0.0")

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

tasks: list[Task] = [
    Task(id=1, title="Learn FastAPI", done=False),
    Task(id=2, title="Deploy to AWS", done=False)
]

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Task API is running"}

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/tasks", response_model=list[Task])
def get_tasks() -> list[Task]:
    return tasks