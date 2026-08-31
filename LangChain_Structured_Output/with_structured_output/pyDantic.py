from langchain_openai import OpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

model=OpenAI()

class Review(BaseModel):
    key_themes:list[str]=Field(description="List down all the important part of the reviews.")
    summary:str=Field(description="Summarize the whole review in few lines")
    sentiment:str=Field(description="Generate the sentiment of review in positive, negative or neutral")
    pros=Optional[list[str]]=Field(default=None, description="If the pros the mentioned then only list down.")
    cons=Optional[list[str]]=Field(default=None, description="If the cons the mentioned then only list down.")

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("The product is good but the software part was installed by too many apps which make the system got hang easily.")

print(result)