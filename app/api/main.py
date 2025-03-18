# app/api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from app.services.services import sum_numbers, average_numbers

app = FastAPI(
    title="Math API",
    description="API RESTful para operações matemáticas (soma e média).",
    version="1.0.0"
)

class NumberList(BaseModel):
    numbers: list[int]


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.post("/sum", summary="Soma uma lista de inteiros", response_model=int)
async def sum_numbers_endpoint(data: NumberList):
    return sum_numbers(data.numbers)

@app.post("/average", summary="Calcula a média de uma lista de inteiros", response_model=float)
async def average_numbers_endpoint(data: NumberList):
    try:
        return average_numbers(data.numbers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))