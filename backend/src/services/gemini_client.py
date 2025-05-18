import os

from google import genai
from google.genai.types import HttpOptions, LiveConnectConfig, Modality


class GeminiSession:
    def __init__(self):
        self.client = genai.Client(http_options=HttpOptions(api_version="v1beta1"))

    def start_session(self):
        config = LiveConnectConfig(response_modalities=[Modality.AUDIO])
        return self.client.aio.live.connect(
            model=os.getenv("MODEL", "gemini-2.0-flash-live-preview-04-09"),
            config=config,
        )
