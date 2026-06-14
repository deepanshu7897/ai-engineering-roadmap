import asyncio
import time

import aiohttp


URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]


async def fetch(
    session: aiohttp.ClientSession,
    url: str,
) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def concurrent_fetch() -> list[dict]:
    timeout = aiohttp.ClientTimeout(total=5)

    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:
        tasks = [
            fetch(session, url)
            for url in URLS
        ]

        return await asyncio.gather(*tasks)


async def sequential_fetch() -> list[dict]:
    timeout = aiohttp.ClientTimeout(total=5)

    results = []

    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:
        for url in URLS:
            result = await fetch(
                session,
                url,
            )
            results.append(result)

    return results


async def main() -> None:
    start = time.perf_counter()

    await sequential_fetch()

    sequential_time = (
        time.perf_counter() - start
    )

    start = time.perf_counter()

    await concurrent_fetch()

    concurrent_time = (
        time.perf_counter() - start
    )

    print(
        f"Sequential: {sequential_time:.2f}s"
    )

    print(
        f"Concurrent: {concurrent_time:.2f}s"
    )


if __name__ == "__main__":
    asyncio.run(main())