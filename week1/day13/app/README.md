# Day 13 – Async Routes & Background Tasks

## Topics Covered

- async def
- BackgroundTasks
- asyncio
- run_in_executor
- Lifespan Events
- app.state
- Startup & Shutdown

## Endpoints

GET /

POST /process

## Run

```bash
uvicorn main:app --reload
```

## Result

The API immediately returns a Job ID while document processing continues asynchronously in the background.