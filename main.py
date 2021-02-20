from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from src import __version__
from src.api.api import api_router

app = FastAPI(version=__version__)
app.include_router(api_router, prefix="/api", tags=["api"])

templates = Jinja2Templates(directory="templates")
app.mount("/media", StaticFiles(directory=r"/home/septimo/static"), name="media")
app.mount("/static", StaticFiles(directory="templates/static"), name="static")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/movie/{file}")
def index(request: Request, file: str):
    return templates.TemplateResponse("movie.html", {"request": request, "file": file})