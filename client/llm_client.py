from openai import AsyncOpenAI
from typing import Any


class LLMClient:
    def __init__(self) -> None:
        self._client: AsyncOpenAI | None = None

    def get_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                base_url="http://localhost:11434/v1", api_key="ollama"
            )
        return self._client

    async def close(self) -> None:
        if self._client:
            await self._client.close()
            self._client = None

    async def chat_completion(self, message: list[dict[str, Any]], stream: bool = True):
        pass
