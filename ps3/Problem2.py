import math
import random

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def get_frequency_dict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x ,0) + 1
    return freq


def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()



def deal_hand(n):

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels-1,num_vowels):
        x='*'
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

# print(get_frequency_dict('hubba babba'))
# display_hand(get_frequency_dict('hubba babba'))
# display_hand({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1})
# print(SCRABBLE_LETTER_VALUES.get('m',4)+2)

newhand=deal_hand(6)
print(newhand)
display_hand(newhand)



def update_hand(hand, word):
    hand_copy=hand.copy()
    for i in word:
        if i in hand_copy.keys():
            hand_copy[i]=hand_copy.get(i,0)-1
            if hand_copy[i]==0:
                del hand_copy[i]
    return hand_copy

# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# hand={'j':2, 'o':1, 'l':1, 'w':1, 'n':2}
# display_hand(hand)
# new_hand = update_hand(hand, 'jolly')
# print(new_hand)
# display_hand(new_hand)