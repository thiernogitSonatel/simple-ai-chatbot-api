from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Simple AI Chatbot API",
              description="A minimal AI-like chatbot API built with FastAPI.",
              version="1.0.0")

app.include_router(router)
