import openai

from os import getenv
from dotenv import load_dotenv
from config import *

load_dotenv()

def create_dialog(msg):
    token = getenv('API')
    openai.api_key = token

    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=msg,
        max_token=100,
        top_p=1,
        stop=None,
        temperature=0.5
    )

    response = completion.choices[0].text
    return response

def test():
    rp = create_dialog(CHAT_2)
    print(rp)

test()

def return_dialog(msg):
    response = create_dialog(msg)
    return response

def chat_1():
    response = return_dialog(CHAT_1)
    return response

def chat_2():
    response = create_dialog(chat_1())
    return response

#print(f"CHAT-1:\n    {chat_1()}")
#print(f"CHAT-2:\t{chat_2()}")
