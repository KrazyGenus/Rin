from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/a2a/parcel")
async def a2a_endpoint(request: Request):
    print("i was hit son!")
    
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    PORT = 8000
    uvicorn.run(app, host="0.0.0.0", port=PORT)