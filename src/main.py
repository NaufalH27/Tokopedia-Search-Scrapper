from fastapi import FastAPI
from api import api_router
import uvicorn

app = FastAPI()

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)