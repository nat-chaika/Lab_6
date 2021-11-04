"""
Target game in Ukrainian language
"""
import random


def generate_grid():
    """
    -> list[str]
    Generate list of five unick ukrainian letters
    """
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    letters = []
    while len(letters) != 5:
        letter = random.choice(alphabet)
        if letter in letters:
            pass
        else:
            letters.append(letter)
    return letters
# print(generate_grid())
