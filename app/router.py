from fastapi import APIRouter
from app.model import generate_response

router = APIRouter()

@router.post("/chat")
def chat(message: dict):
    user_input = message.get("text", "")
    response = generate_response(user_input)
    return {"user": user_input, "bot": response}
