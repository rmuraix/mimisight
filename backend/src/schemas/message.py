from pydantic import BaseModel


class ImageData(BaseModel):
    mime_type: str
    data: str  # base64文字列


class AudioData(BaseModel):
    mime_type: str
    data: str  # base64文字列
