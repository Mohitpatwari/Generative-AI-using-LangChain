from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1=PromptTemplate(
    template="Write a tweet for the topic {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Write a linkedin post for the topic {topic}",
    input_variables=['topic']
)

model=ChatOpenAI()
parser=StrOutputParser()

chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkedin':RunnableSequence(prompt2, model, parser)
})

result=chain.invoke({'topic':'Cricket'})
print(result)