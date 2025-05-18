import asyncio
import base64

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from google.genai.types import Blob, Content, Part

from src.schemas.message import AudioData, ImageData
from src.services.gemini_client import GeminiSession

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "FastAPI is working!"}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async with GeminiSession().start_session() as session:
        try:
            receive_task = asyncio.create_task(receive_response(session, websocket))

            while True:
                msg = await websocket.receive_json()

                # テキスト入力
                if "text" in msg:
                    content = Content(role="user", parts=[Part(text=msg["text"])])
                    await session.send_client_content(turns=content)

                # 画像入力
                elif "image" in msg:
                    image = ImageData(**msg["image"])
                    binary = base64.b64decode(image.data)

                    blob = Blob(data=binary, mime_type=image.mime_type)

                    await session.send_realtime_input(media=blob)

                # 音声入力
                elif "audio" in msg:
                    audio = AudioData(**msg["audio"])
                    audio_bytes = base64.b64decode(audio.data)

                    blob = Blob(data=audio_bytes, mime_type=audio.mime_type)
                    await session.send_realtime_input(media=blob)

                else:
                    await websocket.send_json({"error": "Invalid message format"})

        except WebSocketDisconnect:
            receive_task.cancel()
            await session.close()


async def receive_response(session, websocket: WebSocket):
    async for response in session.receive():
        if response.data:
            await websocket.send_json(
                {"audio": base64.b64encode(response.data).decode()}
            )
