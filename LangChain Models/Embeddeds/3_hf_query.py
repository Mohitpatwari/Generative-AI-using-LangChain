from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name="Write your model name here.")

result=embeddings.embed_query("What is your name?")
print(str(result))