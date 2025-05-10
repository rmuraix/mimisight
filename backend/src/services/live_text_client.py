import os

from google import genai
from google.genai.types import (
    Content,
    HttpOptions,
    LiveConnectConfig,
    Modality,
    Part,
)

client = genai.Client(http_options=HttpOptions(api_version="v1beta1"))
MODEL_ID = os.getenv("MODEL_ID", "gemini-2.0-flash-live-preview-04-09")


async def get_text_response_live(prompt: str) -> str:
    response_parts = []

    async with client.aio.live.connect(
        model=MODEL_ID,
        config=LiveConnectConfig(response_modalities=[Modality.TEXT]),
    ) as session:
        await session.send_client_content(
            turns=Content(role="user", parts=[Part(text=prompt)])
        )

        async for message in session.receive():
            if message.text:
                response_parts.append(message.text)

    return "".join(response_parts) if response_parts else "[No response]"
