import traceback

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import uvicorn

app = FastAPI(
    docs_url="/api-docs",
    redoc_url="/api-redoc",
)


class AttendanceItem(BaseModel):
    name: str
    student_number: str


@app.get("/")
def read_root():
    return {"message": "Hello TAPIE"}


@app.get("/hello-world")
async def say_hello(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")
    headers = {"Access-Control-Allow-Origin": "http://localhost:5500"}
    return JSONResponse(content={"message": f"Hello {name}"}, headers=headers)


@app.post("/attendance")
async def read_item(data: AttendanceItem):
    if not data.name or not data.student_number:
        raise HTTPException(
            status_code=400, detail="Name and student number are required"
        )
    print(f"{data.student_number} {data.name} 출석체크됨.")
    headers = {"Access-Control-Allow-Origin": "http://localhost:5500"}
    return JSONResponse(content={"message": f"{data.student_number} {data.name} 출석체크됨."}, headers=headers)


@app.get("/try-cors-error")
async def try_cors_error():
    headers = {"Access-Control-Allow-Origin": "http://notallowed-origin.com"}
    return JSONResponse(content={"message": "Try CORS Error"}, headers=headers)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
