from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()
data = PyPDFLoader("documents loader/Sarosh_Resume (1).pdf")
docs=data.load()
template=ChatPromptTemplate([
    ("system","You are the AI that Gives contact details"),
    ("human","{data}")
])
model = init_chat_model("groq:openai/gpt-oss-120b")
# model = init_chat_model("google_genai:gemini-3.5-flash",temperature=1)

prompt=template.format_messages(data=docs[0].page_content)
response=model.invoke(prompt)
print(response.content)
