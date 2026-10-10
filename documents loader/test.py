from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
data = PyPDFLoader("documents loader/Sarosh_Resume (1).pdf")
#data=TextLoader("path/")
docs=data.load()
print(docs[0].page_content)