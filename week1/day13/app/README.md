# Day 13 - Async Routes & Background Tasks

## Topics Covered

- Async Routes
- BackgroundTasks
- asyncio
- Lifespan Events
- Startup & Shutdown
- FastAPI Background Processing

## Run

```bash
uvicorn main:app --reload
```

## Endpoint

POST /process

## Result

Background task executes after returning the API response.