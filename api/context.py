"""
ChatManager sınıfı, tüm kullanıcıları ve konuşmalarını bir sözlük
şeklinde yönetir.

Her kullanıcı, Google Gemini API'si tarafından sağlanan kullanıcıya ait
birden fazla önceki konuşmayı içerebilen bir ChatConversation örneğine sahiptir.

ImageChatManager sınıfı oldukça basittir çünkü Gemini Pro'daki
resimlerin bağlamsal bir ortamı yoktur. Bu sınıf, adreslere fotoğraf alma
gibi bazı görevleri yerine getirir.
"""
from io import BytesIO
from typing import Dict

import requests

from .config import BOT_TOKEN
from .gemini import ChatConversation, generate_text_with_image


class ChatManager:
    """Temel bir konuşma depolama yöneticisi ayarlama"""

    def __init__(self):
        self.chats: Dict[int, ChatConversation] = {}

    def _new_chat(self, history_id: int) -> ChatConversation:
        chat = ChatConversation()
        self.chats[history_id] = chat
        return chat

    def get_chat(self, history_id: int) -> ChatConversation:
        if self.chats.get(history_id) is None:
            return self._new_chat(history_id)
        return self.chats[history_id]


class ImageChatManager:
    def __init__(self, prompt, file_id: str) -> None:
        self.prompt = prompt
        self.file_id = file_id

    def tel_photo_url(self) -> str:
        """Telegram fotoğraf URL'sini işleme"""
        r_file_id = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={self.file_id}"
        )
        file_path = r_file_id.json().get("result").get("file_path")
        download_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
        return download_url

    def photo_bytes(self) -> BytesIO:
        """Fotoğrafı baytlara dönüştürme"""
        photo_url = self.tel_photo_url()
        response = requests.get(photo_url)
        photo_bytes = BytesIO(response.content)
        return photo_bytes

    def send_image(self) -> str:
        response = generate_text_with_image(self.prompt, self.photo_bytes())
        return response
