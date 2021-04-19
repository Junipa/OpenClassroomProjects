medicaments = ["Aspiron", "Rhinoplexil"]
clients = ["Malfichu", "Palichon"]
stocks = [13, 7]
credit = [0, 0]

def lireMedicament(medicaments):
    medicament = input("Nom du médicament ? ").capitalize()
    while medicament not in medicaments :
            medicament = input("Veuillez saisir le nom d'un médicament en stock. ").capitalize()
    return medicament

def lireClient(clients):
    client = input("Nom du client ? ").capitalize()
    if client.isalpha()==True and client not in clients:
            clients.append(client.capitalize())
            credit.append(0)
    else:
        while client not in clients:
            client = input("Veuillez saisir le nom du client. ")
    return client

def affichage(clients, medicaments):
    print("Affichage des stocks")
    for medicament in medicaments :
        stock = stocks[medicaments.index(medicament)]
        print("Stock du médicament {} : {}".format(medicament, stock))
    print("Affichage des crédits")
    for client in clients:
        cred = credit[clients.index(client)]
        print("Crédit du client {} : {}".format(client, cred))
    print("\n\n")

def achat(clients, medicaments):
    client = lireClient(clients)
    medicament = lireMedicament(medicaments)
    paiement = int(input("Quel est le montant du paiement ? "))
    credit[clients.index(client)] += paiement
    quantite = int(input("Quelle est la quantité achetée ? "))
    stocks[medicaments.index(medicament)] -= quantite

def approvisionnement(medicaments):
    medicament = lireMedicament(medicaments)
    quantite = int(input("Indiquez la quantité : "))
    stocks[medicaments.index(medicament)] += quantite

def pharmacie(clients, medicaments):
    ans = ""
    while ans != "4":
        ans = input("1 : Achat de medicament\n2 : Approvisionnement en  medicaments\n3 : Etats des stocks et des credits\n4 : Quitter\n")
        if ans == "1":
            achat(clients, medicaments)
        elif ans == "2":
            approvisionnement(medicaments)
        elif ans == "3":
            affichage(clients, medicaments)
    if ans == "4":
        quit()

pharmacie(clients, medicaments)
