import os
import random
import time


def color_text(text, color = "RED"):
    """
    Takes text as string,  and color as string, returns colored text, can be used in terminal.
    """
    # BLUE = '\033[94m'
    # CYAN = '\033[96m'
    # GREEN = '\033[92m'
    # ORANGE = '\033[93m'
    # RED = '\033[91m'
    if color == "RED":
        return '\033[91m'+text+'\033[0m'

    elif color == 'ORANGE':
        return '\033[93m'+text+'\033[0m'

    elif color == 'GREEN':
        return '\033[92m'+text+'\033[0m'

    elif color == 'CYAN':
        return '\033[96m'+text+'\033[0m'

    elif color == 'BLUE':
        return '\033[94m'+text+'\033[0m'

print(color_text('xd', 'GREEN'))

WIDTH = 20
HEIGHT = 10
