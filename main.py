from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from front.view import router as routerFront

from backend.login.view import router as routerLogin
from backend.ideas.view import router as routerIdeas
from backend.downloader.view import router as routerDownloader

import yfinance as yf

app = FastAPI()

app.include_router(routerFront, prefix="/front")
app.include_router(routerLogin, prefix="/login")
