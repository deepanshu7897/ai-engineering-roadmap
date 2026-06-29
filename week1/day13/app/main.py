import asyncio
import uuid
from contextlib import asynccontextmanager

from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel


class Document(BaseModel):
    title: str
    content: str


processor = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global processor

    processor = "Mock Document Processor"

    print("Processor Started")

    yield

    print("Processor Shutdown")


app = FastAPI(
    title="FastAPI Day 13",
    lifespan=lifespan,
)


async def process_document(
    job_id: str,
    document: Document,
):
    await asyncio.sleep(2)

    print(
        f"Completed Job {job_id} -> {document.title}"
    )


@app.get("/")
async def home():
    return {
        "processor": processor
    }


@app.post("/process")
async def process(
    document: Document,
    background_tasks: BackgroundTasks,
):
    job_id = str(uuid.uuid4())

    background_tasks.add_task(
        process_document,
        job_id,
        document,
    )

    return {
        "message": "Processing Started",
        "job_id": job_id,
    }