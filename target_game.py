from typing import List


def generate_grid() -> List[List[str]]:
    import random
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = []
    grid = []
    for i in range(9):
        letters.append(chr(random.randint(ord('A'), ord('Z'))))
    for i in range(0, (len(letters)), 3):
        stock = []
        stock.append(letters[i])
        stock.append(letters[i+1])
        stock.append(letters[i+2])
        grid.append(stock)
    return grid
# print(generate_grid())


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words = []
    dict = open(f, 'r')
    content = dict.read()
    words = content.split("\n")
    dict.close()
    del words[0]
    del words[0]
    del words[0]
    words_best = []
    for i in range(len(words)):
        words[i] = words[i].lower()
        if 3 < len(words[i]) < 10 and letters[4] in words[i]:
            let = list(words[i])
            values = []
            for k in range(len(let)):
                sig = words[i].count(let[k])
                values.append(sig)
            k = 0
            dictionary1 = {}
            for u in let:
                dictionary1[u] = values[k]
                k += 1
            # print(dictionary1)
            val = []
            for b in range(len(letters)):
                lette = "".join(letters)
                fab = lette.count(letters[b])
                val.append(fab)
            j = 0
            dictionary2 = {}
            for c in letters:
                dictionary2[c] = val[j]
                j += 1
            # print(dictionary2)
            crak = 0
            for el in dictionary1:
                # print(el)
                if (el in dictionary2) and dictionary1[el] <= dictionary2[el]:
                    crak += 1
            if crak == len(dictionary1):
                    words_best.append(words[i])
            
    return words_best
# print(get_words("en1.txt", ["r", "a", "u", "n", "r", "f", "a", "e", "o"]))

