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


def get_words(fff, letters):
    """
    (str, list[str]) -> list[tuple(str, str)]

    Read the file and check words in file with the rules.
    Rules are: words should be shorter than 5 letters,
    and start with one of the letters from list
    """

    words = []
    dict = open(fff, 'r', encoding='utf-8')
    content = dict.read()
    words = content.split("\n")
    dict.close()
    # for i in range(20):
    #     print(words[i])
    words_better = []
    # mark = 0
    # print(len(words))
    for i in range(len(words)-1):
        sigh = 0
        mark = 0
        for kill in range(len(words[i])):
            if mark == 32:
                sigh = kill
                break
            mark = ord(words[i][kill])
        if sigh < 7 and words[i][0] in letters:
            words_better.append(words[i])
    lett_word = []
    keys = []
    for i in range(len(words_better)):
        for kill in range(len(words_better[i])):
            mark = 0
            sigh
            for kill in range(len(words_better[i])):
                if mark == 32:
                    break
                mark = ord(words_better[i][kill])
        lepta = words_better[i][:kill-1]
        lett_word.append(lepta)
        keys.append(words_better[i][kill:])
    for i in range(len(keys)):
        if "/n" in keys[i] or "noun" in keys[i]:
            keys[i] = "noun"
        elif "/v" in keys[i] or "verb" in keys[i]:
            keys[i] = "verb"
        elif "adj" in keys[i] or "/adj" in keys[i]:
            keys[i] = "adjective"
        elif "adv" in keys[i] or "/adv" in keys[i] and "/v" not in keys[i] and "/adj" not in keys[i]:
            keys[i] = "adverb"
    result = tuple(zip(lett_word, keys))
    final = []
    for i in range(len(result)):
        if "noun" in result[i] or "adjective" in result[i] or "verb" in result[i] or "adverb" in result[i]:
            final.append(result[i])
    return final, len(final)
print(get_words("base.lst", ['й', 'є', 'ю']))

