from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

propmt=PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

model=ChatOpenAI()
parser=StrOutputParser()

chain=propmt | model | parser
result=chain.invoke({"topic" : "Cricket"})
print(result)