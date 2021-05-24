

VOWELS = 'aeiou'
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    if word not in word_list:
        return False
    word=word.lower()
    if '*' in word:
        for i in range(5):
            new_word=word.replace('*',VOWELS[i])
            if new_word in word_list:
                return True
        return False

# word='c*ws'
# hand={'s':1, 'o':1, 'w':1, '*':1, 'c':2}
hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
word = "EVIL"
word_list=['honey']

# print(is_valid_word(word,hand,word_list))

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for i in hand.keys():
        count = hand[i] + count
    return count

print(calculate_handlen(hand))