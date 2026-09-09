from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()
def word_count(text):
    return len(text.split())

prompt=PromptTemplate(
    template="Write a joke for the topic {topic}",
    input_variables=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt, model, parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_counts': RunnableLambda(word_count)
})

final=RunnableSequence(joke_gen_chain, parallel_chain)
print(final)