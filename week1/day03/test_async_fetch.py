import pytest

from async_fetch import concurrent_fetch


@pytest.mark.asyncio
async def test_concurrent_fetch():
    result = await concurrent_fetch()

    assert len(result) == 5