import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SytemMessages
#from langchain_community.chat_models import ChatHuggingFace
#from langchain_community.llms import HuggingFacePipeline
from langchain_openai import ChatOpenAI
from transformers import pipeline

os.environ['CL_HOME'] = 'E:/chatbot_Lang'

load_dotenv()

model = ChatOpenAI()

chat_histoy=[
    SytemMessages(content='You are a helpfull AI assistent')
]

while True:
    user_input = input('You:')
    chat_histoy.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_histoy)
    chat_histoy.append(AIMessage(content=result))
    print("AI:",result.content)

print(chat_histoy)