import os

from google import genai
from google.genai.types import HttpOptions, LiveConnectConfig, Modality


class GeminiSession:
    """
    GeminiSession manages a connection to the Gemini AI service using the genai client.

    Methods:
        __init__():
            Geminiセッションを初期化

        start_session():
            ライブセッションを開始し、Geminiモデルと接続
            Returns:
                Geminiモデルと対話するための非同期接続オブジェクト
    """
    def __init__(self):
        self.client = genai.Client(http_options=HttpOptions(api_version="v1beta1"))

    def start_session(self):
        config = LiveConnectConfig(response_modalities=[Modality.AUDIO])
        return self.client.aio.live.connect(
            model=os.getenv("MODEL_NAME", "gemini-2.0-flash-live-preview-04-09"),
            config=config,
        )
