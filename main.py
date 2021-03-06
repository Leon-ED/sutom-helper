# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def nettoyer_mot(mot,caracteres_interdits):
    new_mot = ""
    for lettres in mot:
        if lettres not in caracteres_interdits:
            new_mot += lettres
    return new_mot


def nettoyer_dico(lien,longueur):
    '''Ecrit dans le fichier dico.txt les mots etant uniquement de la longueur entrée par l'utilisateur'''
    with open(lien,"r") as fichier:
        with open("./dico.txt","w") as dico:
            for lignes in fichier:
                lignes = lignes.strip()
                mots = nettoyer_mot(lignes,[",","\n",',','"'])
                if len(mots) == longueur:
                    dico.write(mots+"\n") 


def liste_mots(lien):
    mots = []
    with open(lien,'r') as fichier:
        for lignes in fichier:      
            mots.append(lignes.strip().split("\n")[0])
    return mots



def trouver_mot(lettres_ordonnes,dico,lettres=[],not_here=[]):
    '''Entrer un liste de taille 6 avec 9 pour les positions inconnues'''
    new_lettres = []
    i = 0
    for lettre in lettres_ordonnes:
        if lettre != '9' and lettre != "*" :
            new_lettres.append([lettre,i])
        i += 1
    mots_potentiels = []
    for mots in dico:
        mots = mots.lower()
        coup = 0

        for lettre,index in new_lettres:
            if mots[index] == lettre.lower():
                coup += 1

        for lettre in lettres:
            if lettre == "*":
                coup += 1
            if lettre.lower() in mots:
                coup += 1

        for lettre in not_here:
            if lettre.lower() not in mots:
                coup+=1

        if coup == len(new_lettres)+len(lettres)+len(not_here):
            mots_potentiels.append(mots)
    
    return mots_potentiels



def affichage():
    longueur = 0
    print("====== RESOLUTION DE SUTOM =======")

    while True:
        try:
            longueur = int(input("Entrer la longueur du mot :"))
            break
        except ValueError:
            print("Réessayer en entrant un entier comme valeur !")
        
    print("Entrer la liste des lettres")
    print("(sous forme : PR***T) mettre un * pour les lettres inconnues")

    lettres_ordonnes = str(input("Entrer lettres : "))
    print("=====")
    lettres_desordonnes = str(input("Entrer maintenant les lettres dont la position est inconnue \n forme : ABC "))
    not_here = str(input("Entrer les lettres qui ne sont pas dans le mot : "))

    return lettres_ordonnes,lettres_desordonnes,longueur,not_here




def main(donnes):
    longueur, lettres_ordonnes,lettres_desordonnes,not_here = donnes
    nettoyer_dico("./mot.txt",longueur)
    mots = liste_mots("./dico.txt")

    listeResultat = trouver_mot(lettres_ordonnes,mots,lettres_desordonnes,not_here)
    print("\n=========== SUTOM Helper ==============")
    if listeResultat == []:

        print("Aucun mot trouvé ! Vérifier les informations entrées")
    else:
        print(f"Résultat {len(listeResultat)} mots ont été trouvés")
        print(trouver_mot(lettres_ordonnes,mots,lettres_desordonnes,not_here))
        print("Si la liste est longue réessayer en entrant plus d'informations")

    


if __name__ == "__main__":

    try:
        donnes = int(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4])
    except IndexError :
        print("Attention arguments manquants ! :")
        print("Passage en mode manuel ")
        donnes = affichage()
    except ValueError:
        print("Attention erreur dans les arguments ! :")
        print("Passage en mode manuel ")
        donnes = affichage()
    main(donnes)