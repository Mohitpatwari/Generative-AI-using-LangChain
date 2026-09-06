from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a short clean notes for the text {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="Generate question and answers for the quiz on text {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the notes and quiz in one document\n notes->{notes} quiz->{quiz}",
    input_variables=['notes', 'quiz']
)

model1=ChatOpenAI()
model2=ChatAnthropic()

parser=StrOutputParser()

parallel=RunnableParallel({
   'notes': prompt1 | model1 | parser,
   'quiz': prompt2 | model2 | parser
})

sequence=prompt3 | model1 | parser

chain=parallel | sequence
result=chain.invoke({'text' : "Enter your document"})
print(result)