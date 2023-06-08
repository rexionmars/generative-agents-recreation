import openai

from os import getenv
from config import *

from dotenv import load_dotenv
load_dotenv()

def create_dialog(msg):
    """
    Create a dialog from a message
    """
    token = getenv('API')
    openai.api_key = token

    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=msg,
        max_tokens=2048,
        stop=None,
        n=1,
        temperature=0.8
    )

    response = completion.choices[0].text
    return response
