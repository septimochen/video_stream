from fastapi import APIRouter
from src.api.endpoints import vods

api_router = APIRouter()
api_router.include_router(vods.router, prefix="/vods", tags=["Vods"])