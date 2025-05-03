from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.utility.llama_utils import chat_with_llama2

router = APIRouter()

class ConversationRequest(BaseModel):
    prompt: str

@router.post("/conversation")
async def conversation_view(request: ConversationRequest):
    """
    Endpoint to initiate a conversation with the AI model (Llama2).
    """
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Request is empty.")

    response = chat_with_llama2(request.prompt)

    return {"success": True, "ai": response, "message": "Conversation completed successfully"}
