from fastapi import APIRouter

router = APIRouter()

@router.get("/traffic")
def get_traffic():
    return [
        {"ip": "192.168.1.1", "usage": 120},
        {"ip": "192.168.1.2", "usage": 80},
        {"ip": "192.168.1.3", "usage": 200}
    ]