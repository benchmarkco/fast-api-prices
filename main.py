from fastapi import FastAPI, Request, Form
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
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/stock_info/{stock}")
async def get_stock_info(stock: str):
    # Use yfinance to retrieve the stock data for the last 30 days
    stock_data = yf.download(stock, period="1mo")

    # Convert the stock data to a JSON format
    stock_data_json = stock_data.to_json(orient="columns")

    # Return the stock data as a JSON response
    return {"symbol": stock, "time_series_data": stock_data_json}

 
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Access the parameters
    name = item.name
    password = item.password

    # Process the data and return a response
    # ...
    print(name)
    return RedirectResponse(url="https://fastapi.tiangolo.com/")



