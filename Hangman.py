"""Hangman"""

"""The computer selects a random 8 letters word within a list."""
from random import randint

#Create word list
"""Sorry, Anas, I didn't change the word list, so all the words are in French... ^^"""
word_list = ["messager", "halogene", "carpette", "etourdir", "abaisser", "abattage", "accoster", "activite", "barbecue"]
#Select a random word
word = word_list[randint(0, len(word_list)-1)]
nb_turn = 0
ascii_art = {
    1 : "_____"
    2 : "\n  |\n  |\n  |\n  |\n  |\n  |\n__|__",
    3 : "\n   _____\n  |\n  |\n  |\n  |\n  |\n  |\n__|__",
    4 : "\n   _____\n  |     |\n  |     |\n  |\n  |\n  |\n  |\n__|__",
    5 : "\n   _____\n  |     |\n  |     |\n  |     o\n  |\n  |\n  |\n__|__",
    6 : "\n   _____\n  |     |\n  |     |\n  |     o\n  |     |\n  |\n  |\n__|__",
    7 : "\n   _____\n  |     |\n  |     |\n  |     o\n  |    /|\n  |\n  |\n__|__",
    8 : "\n   _____\n  |     |\n  |     |\n  |     o\n  |    /|\\\n  |\n  |\n__|__",
    9 : "   _____\n  |     |\n  |     |\n  |     o\n  |    /|\\\n  |    / \n  |\n__|__",
    10 : "   _____\n  |     |\n  |     |\n  |     o\n  |    /|\\\n  |    / \\\n  |\n__|__",
    }

"""Every turn, the player chooses a letter.
If the letter is in the word, the computer outputs the word with the letter found by the player.
The letters not yet found are replaced with '*'.
The player can play 10 turns before losing."""
def hangman(list, nb):
    result = ["*", "*", "*", "*", "*", "*", "*", "*"]
    word2 = []
    for char in word :
        word2.append(char)
    while nb < 10 and '*' in result:
        test = 0
        while test == 0 :
            letter = input("Chose a letter. ")
            if letter.isalpha() == True and len(letter) == 1 :
                test +=1
        letter.lower()
        if letter in word :
            i = 0
            for char in word :
                if letter == char :
                    result[i] = letter
                i+=1
        else :
            print("The letter", letter.upper(), "is not in the word you are looking for.")
            nb +=1
            print(ascii_art[nb])
        result1 = "".join(result)
        print(result1)
        if 10-nb > 1 and '*' in result :
            print("You have", 10-nb, "turns left.")
    if '*' not in result :
        print("Congratulations, you have won !\nThe word was indeed", word.upper(), "!")
    else :
        print("Too bad, you have lost...\nThe word was...", word.upper())

hangman(word_list, nb_turn)
