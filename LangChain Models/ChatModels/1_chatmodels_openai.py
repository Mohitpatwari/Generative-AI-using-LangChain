from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model_openai=ChatOpenAI(model="gpt-4")
result=model_openai.invoke("What is your name?")
print(result)