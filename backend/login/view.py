from fastapi import APIRouter, Request, Response, Form
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/login")
async def login( response: Response, request: Request ,username: str = Form(...), password: str = Form(...)):

    if username == "123a" and password == "123aa":
        response.set_cookie(key="username", value = password)           
        print(request.cookies.get("username"))     
        return RedirectResponse(url="/front/index")
    else:
        return {"message": "Incorrect username or password"}
