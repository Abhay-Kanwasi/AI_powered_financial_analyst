"""
Functions for initializing and configuring language models.
"""
from langchain_groq import ChatGroq
from config import MODEL_NAME, TEMPERATURE

def get_chat_model():
    """
    Initializes and returns a configured ChatGroq model.
    
    Returns:
        ChatGroq: Configured language model
    """
    return ChatGroq(
        temperature=TEMPERATURE,
        model_name=MODEL_NAME
    )
