from fastapi import FastAPI, Request, Form, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import yfinance as yf

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory = "templates")

@app.get("/", response_class = HTMLResponse)
async def front(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/index", response_class = HTMLResponse)
async def front_index(request: Request):
    username = request.cookies.get("username")
    print(username)
    return templates.TemplateResponse("index.html", {"request": request, "username": username})

@app.post("/index", response_class = HTMLResponse)
async def front_index(request: Request):
    username = request.cookies.get("username")
    print(username)
    return templates.TemplateResponse("index.html", {"request": request, "username": username})

@app.get("/stock_info/{stock}")
async def get_stock_info(stock: str):
    # Use yfinance to retrieve the stock data for the last 30 days
    stock_data = yf.download(stock, period="1mo")

    # Convert the stock data to a JSON format
    stock_data_json = stock_data.to_json(orient="columns")

    # Return the stock data as a JSON response
    return {"symbol": stock, "time_series_data": stock_data_json}

 
@app.post("/login")
async def login( response: Response, request: Request ,username: str = Form(...), password: str = Form(...)):

    if username == "123a" and password == "123aa":
        
        response.set_cookie(key="username", value = password)   
        print(request.cookies.get("username"))     
        return RedirectResponse(url="/index")
    else:
        return "Incorrect username or password"




