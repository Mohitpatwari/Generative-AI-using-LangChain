from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative']=Field(description="Give positive or negative sentiment")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Give the sentiment about the feedback {feedback}\n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructionst()}
)

prompt2=PromptTemplate(
    template="Give a response for the positive feedback {feedback}",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Give a response for the negative feedback {feedback}",
    input_variables=['feedback']
)

clasifier_chain=prompt1 | model | parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser)
    (lambda x:x.sentiment=='negative', prompt3 | model | parser)
    RunnableLambda(lambda x:"No sentiment are received!")
)

chain=clasifier_chain | branch_chain
print(chain)