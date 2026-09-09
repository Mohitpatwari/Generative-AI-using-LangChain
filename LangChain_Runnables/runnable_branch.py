from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a detailed reprt on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarize the given text {text}",
    input_variables=['text']
)

model=ChatOpenAI()
parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1, model, parser)
parallel_chain=RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final=RunnableSequence(report_gen_chain, parallel_chain)
print(final)