from fastapi import FastAPI
import yfinance as yf


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/hello")
async def hello():
    return {"message": "Hello, santiiii!"}

@app.get("/stock_info/{stock}")
async def get_stock_info(stock: str):
    # Use yfinance to retrieve the stock data for the last 30 days
    stock_data = yf.download(stock, period="1mo")

    # Convert the stock data to a JSON format
    stock_data_json = stock_data.to_json(orient="columns")

    # Return the stock data as a JSON response
    return {"symbol": stock, "time_series_data": stock_data_json}