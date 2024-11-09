from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

def get_model():
    load_dotenv("./keys.env")
    groq_key=os.getenv("GROQ_API_KEY")
    llm=ChatGroq(
        model_name="llama-3.1-70b-versatile",
        groq_api_key=groq_key,
        temperature=0,
        max_tokens=1000,
        timeout=None,
        max_retries=2
    )
    
    return llm
