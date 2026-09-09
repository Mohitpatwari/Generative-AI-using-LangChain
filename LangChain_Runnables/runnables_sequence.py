from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template="Write a joke for the topic {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Write a complete explanation about the joke {text}",
    input_variables=['text']
)

model=ChatOpenAI()

parser=StrOutputParser()

chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result=chain.invoke({'topic':'Cricket'})
print(result)