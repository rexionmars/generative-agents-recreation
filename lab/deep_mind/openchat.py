import openai

from os import getenv
from config import *

from dotenv import load_dotenv
load_dotenv()

def create_dialog(msg):
    token = getenv('API')
    openai.api_key = token

    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=msg,
        max_tokens=1024,
        top_p=1,
        stop=None,
        temperature=0.8
    )

    response = completion.choices[0].text
    return response
