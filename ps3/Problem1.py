SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def word_score(word, n):
    score = 0
    wordLength=len(word)
    word=word.lower()
    score2=((7*wordLength)-3*(n-wordLength))
    for i in word:
        if i in SCRABBLE_LETTER_VALUES:
            score=SCRABBLE_LETTER_VALUES[i]+score
    if score2>1:
        return score*score2
    else:
        return score
# print(get_word_score('weed',6))
