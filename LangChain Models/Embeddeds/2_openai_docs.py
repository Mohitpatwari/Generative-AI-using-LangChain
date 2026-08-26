from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents=[
    "What is your name?",
    "What is your age?",
    "What is your role?"
]

model=OpenAIEmbeddings(model="gpt-3.5-large", dimensions=32)
result=model.embed_documents(documents=documents)
print(str(result))