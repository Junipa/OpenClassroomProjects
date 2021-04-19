"""Jeu du pendu"""

"""L'ordinateur choisit un mot de huit lettres maximum au hasard dans une liste."""
from random import randint

word_list = ["abaisser", "abattage", "ablation", "ablution", "accoster", "activite", "araignee", "baguette", "barbecue", "calisson", "carpette", "chausson", "chocolat", "crevette", "douzaine", "elephant", "escargot", "etourdir", "halogene", "herisson", "messager", "religion", "saucisse"]
word = word_list[randint(0, len(word_list)-1)]
nb_coup = 0
score = 0
ascii_art = {
    1 : "_____",
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

"""À chaque coup, le joueur saisit une lettre.
Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres trouvées.
Celles qui ne le sont pas encore sont remplacées par des étoiles (*).
Le joueur a 10 chances ; au delà, il a perdu."""

def start():
    print("Bienvenue dans le jeu du Pendu!",
          "\nVous devez retrouver le bon mot en devinant les 8 lettres qui le composent.")

def hangman(list, nb, score):
    result = ["*", "*", "*", "*", "*", "*", "*", "*"]
    word2 = []
    letters = []
    for char in word :
        word2.append(char)
    while nb < 10 and '*' in result:
        test = 0
        while test == 0 :
            letter = input("Choisissez une lettre. ")
            if letter.isalpha() == True and len(letter) == 1 :
                test +=1
        letter.lower()
        letters.append(letter)
        if letter in word :
            i = 0
            for char in word :
                if letter == char :
                    result[i] = letter
                i+=1
        else :
            print("La lettre", letter.upper(), "n'est pas dans le mot recherché.")
            nb +=1
            print(ascii_art[nb])
        result1 = "".join(result)
        print(result1, "    Lettres utilisées :", letters)
        if 10-nb >= 1 and '*' in result :
            print("Il vous reste", 10-nb, "coups.")
    if '*' not in result :
        score += 10-nb
        print("Félicitations, vous avez gagné !\nLe mot était bien", word.upper(), "!")
    else :
        print("Dommage, vous avez perdu...\nLe mot était...", word.upper())
    print("Votre score est : ", score)

def play_again():
    play = input("Voulez-vous rejouer ? Si oui, tapez O. Sinon, tapez N. ")
    play.lower()
    if play == "o" :
        hangman(word_list, nb_coup, score)
    else :
        quit()

start()
hangman(word_list, nb_coup, score)
play_again()
