from fastapi import FastAPI
from pprint import pprint
from check import check_price

app = FastAPI()
@app.get("/")
async def root():
    return {"test":"Biba"}

res = check_price("DAILY", "RUB", "USD")
pprint(res)