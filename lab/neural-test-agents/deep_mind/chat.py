import openai

from os import getenv
from config import *
from dotenv import load_dotenv
load_dotenv()

def create_dialog(msg):
    token = getenv('API')
    openai.api_key = token

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg,
        max_tokens=2048,
        stop=None,
        n=1,
        temperature=0.8
    )

    return response['choices'][0]['text'].strip()

def newton_mind():
    ...

def einsten_mind():
    ...

def main_chat():
    print('NITRO v0.1.0')

if __name__ == "__main__":
    main_chat()
