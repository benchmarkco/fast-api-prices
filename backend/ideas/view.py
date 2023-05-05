from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/protected")
async def protected(request: Request):
    # Get the value of the "username" cookie from the request
    username = request.cookies.get("username")
    if username:
        return {"message": f"Welcome, {username}!"}
    else:
        return {"error": "You are not authorized to access this page."}
