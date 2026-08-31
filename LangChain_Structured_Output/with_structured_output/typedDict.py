from langchain_openai import OpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model=OpenAI()

class Review(TypedDict):
    Key_themes:Annotated[list[str], "List down all the important part of the reviews."]
    summary:Annotated[str,"Summarize the whole review in few lines"]
    sentiment:Annotated[str, "Generate the sentiment of review in positive, negative or neutral"]
    pros:Annotated[Optional[list[str]], "If the pros the mentioned then only list down."]
    cons:Annotated[Optional[list[str]], "If the cons the mentioned then only list down."]

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("The product is good but the software part was installed by too many apps which make the system got hang easily.")

print(result)