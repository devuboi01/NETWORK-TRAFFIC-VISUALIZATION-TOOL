from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.websocket("/ws/traffic")
async def traffic(websocket: WebSocket):
    await websocket.accept()
    print("CLIENT CONNECTED")

    while True:
        data = {
            "ip": "192.168.1.1",
            "usage": random.randint(50, 500)
        }

        await websocket.send_json(data)
        await asyncio.sleep(1)