from tabnanny import check
from fastapi import FastAPI
from pprint import pprint
from check import check_price
from fastapi.responses import JSONResponse

app = FastAPI()
@app.get("/{interval}/{first_value}/{to_value}/")
async def root(interval: str, first_value: str, to_value: str) -> dict:
    res = check_price("DAILY", first_value, to_value)
    return res