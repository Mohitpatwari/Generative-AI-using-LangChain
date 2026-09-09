from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write a summary of the document {text}",
    input_variables=['text']
)

chain=prompt | model | parser

loader=TextLoader('Pasted text(1).txt', encoding='utf-8')
docs=loader.load()

result=chain.invoke({'text':docs[0].page_content})

print(result)