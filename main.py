from fastapi import FastAPI

from front.view import router as routerFront

from backend.login.view import router as routerLogin
from backend.ideas.view import router as routerIdeas
from backend.downloader.view import router as routerDownloader


app = FastAPI()

app.include_router(routerFront, prefix="/front")

app.include_router(routerLogin, prefix="/login")
app.include_router(routerIdeas, prefix="/ideas")
app.include_router(routerDownloader, prefix="/downloader")
