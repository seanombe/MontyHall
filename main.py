'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com

« Supposez que vous êtes sur le plateau d'un jeu télévisé, face à trois portes
et que vous devez choisir d'en ouvrir une seule, en sachant que derrière l'une
d'elles se trouve une voiture et derrière les deux autres des chèvres.
Vous choisissez une porte, disons la numéro 1, et le présentateur, qui sait,
lui, ce qu'il y a derrière chaque porte, ouvre une autre porte, disons la numéro 3,
porte qui une fois ouverte découvre une chèvre. Il vous demande alors :
« désirez-vous ouvrir la porte numéro 2 ? ». Avez-vous intérêt à changer votre choix ? »
Craig F. Whitaker, Ask Marilyn de Marilyn vos Savant du Parade Magazine en 1990

'''
from enum import Enum
#Pour pouvoir rendre plus explicite la notion de choix nous utiliserons cette abstraction
#Nous définirons stratégie et dirons qu'il y en a deux possibles : changer et garder

from random import *
#L'aléatoire sera généré grace à random

import matplotlib.pyplot as plt



#définition des stratégies
class Strategie(Enum):
    GARDER = 0
    CHANGER = 1

# Simulation d'une seule partie
def partie_unitaire(strategie):

    seed()
    portes = [0,1,2] # Le porte seront représenté par une liste à 3 valeurs possibles
    porte_gagnante = randint(0,2) # La porte gagnante est générée aléatoirement entre 0 1 et 2 (correspondant
    # aux index du tableau de porte)
    choix_de_base_joueur = randint(0,2) # Le choix du joueur est généré aléatoirement entre 0 1 et 2 (correspondant
    # aux index du tableau de porte)

    #Partie logique :

    # Si la stratégie est de Garder
    # Une victoire correspond à ce que le choix du joueur soit celui la porte gagnante
    # Sinon c'est une défaite
    if (strategie == Strategie.GARDER):
        if (portes[porte_gagnante] == choix_de_base_joueur) :
            return True
        else:
            return False

    # Si la stratégie est de Changer
    # Une victoire correspond à ce que le choix du joueur ne pas soit celui la porte gagnante
    # Sinon c'est une défaite
    elif (strategie == Strategie.CHANGER):
        if (portes[porte_gagnante] != choix_de_base_joueur) :
            return True
        else:
            return False


    else:
        return 'Anomalie'

#fonction de répétition d'opérations
def jouer_plusieurs_parties(strategie, nombredeparties):

    liste_des_victoires = []

    for i in range(nombredeparties):
        if partie_unitaire(strategie) == True :
            liste_des_victoires.append(1)
        else :
            liste_des_victoires.append(0)

    return sum(liste_des_victoires)


def main(n):
    # Affichage des résultats via console
    print("Avec la stratégie : Garder, nous gagnons {}/{}"
          .format(jouer_plusieurs_parties(Strategie.GARDER, n), n))
    print("Avec la stratégie : Changer, nous gagnons {}/{}"
          .format(jouer_plusieurs_parties(Strategie.CHANGER, n), n))
#Affichage des résultats via Matplotlib
    plt.figure()
    plt.bar([1,2],[jouer_plusieurs_parties(Strategie.CHANGER, n)/n,
                   jouer_plusieurs_parties(Strategie.GARDER, n)/n],
                   tick_label=["Changer","Garder"])
    plt.title("Monty Hall - Estimation - {} essais".format(n))
    plt.xlabel("Stratégie")
    plt.ylabel("Probabilité")
    plt.show()
    

## Lancement du jeu 10000 FOIS
main(10000)