from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter


# data = PyPDFLoader("documents loader/Sarosh_Resume (1).pdf")
# docs=data.load()
# print(docs[0].page_content)


splitter=CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)
text=TextLoader("documents loader/notes.txt")
text_split=text.load()
chunks=splitter.split_documents(text_split)
for i in chunks:
    print(i.page_content)
    print()
    print()
