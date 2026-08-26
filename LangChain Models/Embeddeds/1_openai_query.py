from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(model="gpt-3.5-large", dimensions=32)
result=model.embed_query("What is your name?")
print(str(result))