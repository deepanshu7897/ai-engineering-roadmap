import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        response.headers["X-Request-ID"] = request_id

        response.headers["X-Process-Time"] = (
            f"{process_time:.4f}s"
        )

        print(
            f"[{request_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{process_time:.4f}s"
        )

        return response