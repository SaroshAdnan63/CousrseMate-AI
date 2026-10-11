from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader

url="https://www.apple.com/in/iphone/"
data=WebBaseLoader(url)
web=data.load() 
print(web[0].page_content)