from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Llama2 Chat Application",
    description="An AI-powered chat application using FastAPI and Llama2",
    version="1.0.0",
)

""" CORS Middleware """
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""Static files """
app.mount("/static", StaticFiles(directory="static"), name="static",)

""" Routers """

from .api.conversation import router as conversation_router

app.include_router(conversation_router, prefix="/api", tags=["chat"])
