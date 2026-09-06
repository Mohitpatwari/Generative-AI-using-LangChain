from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

Prompt1=PromptTemplate(
    template="Generate a detailed report about {topic}",
    input_variables=['topic']
)

Prompt2=PromptTemplate(
    template="Generate a 5 lines summary for the text {text}",
    input_variables=['text']
)

model=ChatOpenAI()
parser=StrOutputParser()

chain=Prompt1 | model | parser | Prompt2 | model | parser
result=chain.invoke({'topic' : 'Unemployment in India'})

print(result)