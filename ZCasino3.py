# -*-coding:utf-8-*

from random import randrange
from math import ceil

# portefeuille du joueur
wallet = int(input("De quelle somme disposez-vous ? "))
bet = 0
ans = "Y"

def roulette(wallet, bet, ans):  
    while ans != "N" and wallet > 1 :
        try :
            ans = input("Souhaitez-vous jouer à la roulette ? Appuyez sur Y pour oui ou sur N pour non. ")
            ans = ans.capitalize()
            assert ans == "Y" or ans == "N"
        except AssertionError :
            print("Réponse invalide, veuillez saisir \'Y\' ou \'N\'.")
            ans = input("Souhaitez-vous jouer à la roulette ? Appuyez sur Y pour oui ou sur N pour non. ")
        #mise du joueur :
        bet = int(input("Sur quel numéro souhaitez-vous miser ? "))-1
        try :
            assert bet >= 0 and bet < 50
        except AssertionError :
            print("Veuillez entrer un numéro compris entre 1 et 50.")
            bet = int(input("Sur quel numéro souhaitez-vous miser ? "))-1
        mise = int(input("Quelle somme souhaitez-vous miser ? "))
        try :
            assert mise > 0
        except :
            print("Votre mise doit être supérieure à 0$.")
            mise = int(input("Quelle somme souhaitez-vous miser ? "))
        wallet -= mise
        #roulette :
        win_nb = randrange(50)
        print("Le numéro gagnant est le... ", win_nb, " !")
        #result :
        if win_nb == bet :
            print("Vous avez gagné 3 fois votre mise !")
            wallet += mise + 3*mise
        elif (win_nb%2 == 0 and bet%2 == 0) or (win_nb%2!=0 and bet%2 != 0):
            print("Numéro de même couleur, vous gagnez la moitié de votre mise !")
            wallet += mise + ceil(mise/2)
        print("Il vous reste ", wallet, "$.")
    if wallet <=1:
        print("Vous n'avez plus d'argent ! \nFin du programme.")
        exit()
    elif ans == "N" :
        print("Fin du programme.")
        exit()

roulette(wallet, bet, ans)


