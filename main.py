from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/a2a/parcel")
async def a2a_endpoint(request: Request):
    print("i was hit son!")