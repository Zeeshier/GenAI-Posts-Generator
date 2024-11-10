from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("why mosts billionaire came from harvard and stanford")
    print(response.content)