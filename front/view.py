from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory = "templates")

@router.get("/login", response_class = HTMLResponse)
async def front(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/home/finance", response_class = HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("finanzas/home.html", {"request": request})

@router.get("/index", response_class = HTMLResponse)
async def front_index_get(request: Request):
    username = request.cookies.get("username")
    print(username)
    return templates.TemplateResponse("index.html", {"request": request, "username": username})

@router.post("/index", response_class = HTMLResponse)
async def front_index(request: Request):
    username = request.cookies.get("username")
    print(username)
    return templates.TemplateResponse("index.html", {"request": request, "username": username})

@router.get("/downloader", response_class = HTMLResponse)
async def front_index(request: Request):
    return templates.TemplateResponse("downloader/index.html", {"request": request})


