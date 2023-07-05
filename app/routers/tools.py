from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """
    Simple ping route

    Returns 'Ping:Pong'
    """
    return {"ping":"pong"}