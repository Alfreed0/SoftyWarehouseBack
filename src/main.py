import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import general_settings
from routes import router

app = FastAPI(
    title="Siemav auth",
    description="",
    version="0.0.1",
)

origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    HOST = general_settings.HOST
    DEBUG = general_settings.DEBUG
    PORT = general_settings.PORT
    APP_NAME = "main:app"
    args = sys.argv[1:]

    if len(args) > 0:
        if "dev" in args:
            DEBUG = True
            os.environ["DEV"] = "True"
        else:
            DEBUG = False
    uvicorn.run(app=APP_NAME, host=HOST, port=PORT, reload=DEBUG)
