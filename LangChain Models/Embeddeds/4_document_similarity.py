from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model="gpt-3-large", dimensions=32)

documents=[
    "The Rose is a popular garden flower known for its sweet smell and thorny stem."
    "A sunflower has a large, bright yellow head that turns to follow the sun."
    "The lotus is a beautiful water plant that grows well in muddy ponds and shallow lakes."
    "Jasmine is a small white or yellow flower that gives off a strong, lovely fragrance at night."
    "Marigold flowers have bright orange and yellow petals that keep bugs away from vegetable gardens."
]

query="Tell me about Sunflower"

doc_embeddings=embedding.embed_documents(documents)
query_embeddings=embedding.embed_query(query)

scores=cosine_similarity([query_embeddings], doc_embeddings)[0]
index, score=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])