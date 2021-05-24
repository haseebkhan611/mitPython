
import random
import string

WORDLIST_FILENAME = "words.txt"
alpbets =string.ascii_lowercase
letters_guessed=[]
check_words=[]
def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code



# Load the list of words into the variable wordlist
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    m=[]
    for i in secret_word:
        if i in letters_guessed:
            m.append(i)
    m1=''.join(m)
    if m1==secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = []
    for i in secret_word:

        present = 0
        for j in letters_guessed:
            if i == j:
                present += 1
        if present == 0:
            guessed_word.append('_')
        else:
            guessed_word.append(i)
    new1 = ' '.join(guessed_word)
    return (new1)


def get_available_letters(letters_guessed):
    fin = []
    for i in alpbets:
        if i not in letters_guessed:
            fin.append(i)
    new2 = ''.join(fin)
    return (new2)


def hangman(secret_word):
    num_of_guess=6
    warnings=0
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    print(" ------------------- ")
    print("You have 6 guesses left.")
    print("Available letters: "+alpbets)

    while is_word_guessed(secret_word, letters_guessed)==False:
        print("You have "+str(num_of_guess)+" guesses left")
        print("Available letters: "+get_available_letters(letters_guessed))
        guessed_letter=input("Please guess a letter: ").lower()
        letters_guessed.append(guessed_letter)

        if (guessed_letter not in alpbets) or (guessed_letter in check_words):
            print("This is your "+str(warnings)+" warning")
            print('Invalid input warning')
            print(" ------------------- ")
            warnings+=1



            if warnings==3:
                warnings=0
                num_of_guess-=1
                print(" ------------------- ")
                print("This was third strike. You lost 1 guess ")

        elif guessed_letter in secret_word:
            print("Good Guess : "+get_guessed_word(secret_word,letters_guessed))
            print(" ------------------- ")
        elif num_of_guess==0:
            print("You ran out of guesses. Better luck next time")
            break
        else:
            print("Oops! That letter is not in my word : "+get_guessed_word(secret_word,letters_guessed))
            print(" ------------------- ")
            num_of_guess -= 1

        check_words.append(guessed_letter)




secret_word=choose_word(wordlist)

hangman(secret_word)