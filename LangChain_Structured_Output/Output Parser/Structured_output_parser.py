from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name="fact1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact3", description="Fact 3 about the topic")
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give three facts about {topic}\n {format_instructions}",
    input_variables=["topic"],
    partial_variables=[{"format_instructions":parser.get_format_instructions()}]
)

prompt=template.invoke({'topic':"Black hole"})
result=model.invoke(prompt)
final_result=parser.parse(result)
print(final_result)