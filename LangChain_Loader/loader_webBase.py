from langchain_community.document_loaders import WebBaseLoader

url="https://claude.ai/chat/af5ef9a2-3c5e-4998-af57-5e2b0813e7dc"
loader=WebBaseLoader(url)
docs=loader.load()

print(docs[0].metadata)