import asyncio
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import BackgroundTasks, FastAPI, Request
from pydantic import BaseModel


# -----------------------------
# Pydantic Model
# -----------------------------

class Document(BaseModel):
    title: str
    content: str


# -----------------------------
# Mock Processor Service
# -----------------------------

class Processor:

    async def chunk_document(self, document: Document):

        print(f"Started processing: {document.title}")

        await asyncio.sleep(2)

        print(f"Chunking completed: {document.title}")


# -----------------------------
# Blocking Task
# -----------------------------

def write_log(job_id: str):

    time.sleep(1)

    print(f"Log written for Job {job_id}")


# -----------------------------
# Lifespan
# -----------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Initializing Processor...")

    app.state.processor = Processor()

    yield

    print("Shutting down Processor...")


# -----------------------------
# FastAPI App
# -----------------------------

app = FastAPI(
    title="FastAPI Day 13",
    lifespan=lifespan,
)


# -----------------------------
# Home
# -----------------------------

@app.get("/")
async def home():

    return {
        "status": "Processor Ready"
    }


# -----------------------------
# Background Processing
# -----------------------------

async def process_document(
    job_id: str,
    document: Document,
    request: Request,
):

    await request.app.state.processor.chunk_document(
        document
    )

    loop = asyncio.get_running_loop()

    await loop.run_in_executor(
        None,
        write_log,
        job_id,
    )

    print(f"Completed Job {job_id}")


# -----------------------------
# Process Endpoint
# -----------------------------

@app.post("/process")
async def process_document_api(
    document: Document,
    background_tasks: BackgroundTasks,
    request: Request,
):

    job_id = str(uuid.uuid4())

    background_tasks.add_task(
        process_document,
        job_id,
        document,
        request,
    )

    return {
        "message": "Processing started",
        "job_id": job_id,
    }