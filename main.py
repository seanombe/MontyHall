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
from random import *


class Strategie(Enum):
    GARDER = 0
    CHANGER = 1


def partie_unitaire(strategie):

    seed()

    portes = [0,1,2]

    porte_gagnante = randint(0,2)

    choix_de_base_joueur = randint(0,2)

    if (strategie == Strategie.GARDER) and (portes[porte_gagnante] == choix_de_base_joueur) :
        return True
    else:
        return False

    if (strategie == Strategie.CHANGER) and (portes[porte_gagnante] == choix_de_base_joueur) :
        return False
    else:
        return True

def jouer_plusieurs_parties(strategie, nombredeparties):

    print(strategie)
    liste_des_victoires = []
    for i in range(nombredeparties):
        if partie_unitaire(strategie) == True :
            liste_des_victoires.append(1)
        else :
            pass
    print(liste_des_victoires)
    return sum(liste_des_victoires)


def main(n):
    #print("Avec la stratégie : Garder, nous gagnons {}/{}"
    #      .format(jouer_plusieurs_parties(Strategie.GARDER, n), n))

    print("Avec la stratégie : Garder, nous gagnons {}/{}"
          .format(jouer_plusieurs_parties(Strategie.CHANGER, n), n))


main(10)