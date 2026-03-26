import pytest
import asyncio
import time
from litellm.timeout import timeout
from litellm.exceptions import Timeout


@timeout(timeout_duration=0.01)
def slow_sync_function(model):
    """A slow synchronous function for testing."""
    time.sleep(0.05)
    return "done"


@timeout(timeout_duration=0.01)
async def slow_async_function(model):
    """A slow asynchronous function for testing."""
    await asyncio.sleep(0.05)
    return "done"


def test_sync_timeout_coverage():
    """Test sync timeout properly catches and assigns llm_provider."""
    with pytest.raises(Timeout) as exc:
        slow_sync_function("test-model")
    assert exc.value.llm_provider == "openai"  # fallback since 'test-model' not recognized or just openai default


@pytest.mark.asyncio
async def test_async_timeout_coverage():
    """Test async timeout properly catches and assigns llm_provider."""
    with pytest.raises(Timeout) as exc:
        await slow_async_function("test-model")
    assert exc.value.llm_provider == "openai"


def test_sync_timeout_exception_coverage():
    """Test sync timeout exception block when model lookup fails."""
    # Pass model=None to force get_llm_provider to raise an Exception
    with pytest.raises(Timeout) as exc:
        slow_sync_function(None)
    assert exc.value.llm_provider == "openai"  # fallback


@pytest.mark.asyncio
async def test_async_timeout_exception_coverage():
    """Test async timeout exception block when model lookup fails."""
    with pytest.raises(Timeout) as exc:
        await slow_async_function(None)
    assert exc.value.llm_provider == "openai"
