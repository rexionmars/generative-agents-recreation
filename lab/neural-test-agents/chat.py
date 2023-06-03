from openchat import create_dialog

from colorama import Fore, Back, Style
from config import *

def chat():
    question = create_dialog(CHAT_1)
    print(f"Aluno: {Fore.YELLOW + question + Style.RESET_ALL}\n")

    response = create_dialog(question)
    print(f"Professor Dimmy:", end="")
    print(Fore.GREEN + response, Style.RESET_ALL + '\n')


for i in range(3):
    chat()
