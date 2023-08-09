from fastapi import FastAPI
from fastapi import UploadFile,File
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping() :
    return "Hello, this is live."

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
) :
    pass

if __name__ == "__main__" :
    uvicorn.run(app,host = 'localhost',port =8000)