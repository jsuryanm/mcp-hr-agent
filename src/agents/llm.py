from langchain_groq import ChatGroq 
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

def get_llm():
    llm = ChatGroq(api_key=api_key,
                   model="openai/gpt-oss-20b",
                   temperature=0,
                   max_tokens=300)
    return llm