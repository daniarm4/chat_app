from typing import Any 

from fastapi.websockets import WebSocket


class WebsocketConnectionManager:
    def __init__(self) -> None:
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, json_data: dict[str, Any]):
        for connection in self.connections:
            await connection.send_json(json_data)
            