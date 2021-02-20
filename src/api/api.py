from fastapi import APIRouter
from src.api.endpoints import vods, actors

api_router = APIRouter()
api_router.include_router(vods.router, prefix="/vods", tags=["Vods"])
api_router.include_router(actors.router, prefix="/actors", tags=["Actors"])