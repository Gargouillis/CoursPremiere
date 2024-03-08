"""
Le programme doit permettre de réaliser 5 actions :

1: Ajouter un élément à la liste de courses

2: Retirer un élément de la liste de courses

3: Afficher les éléments de la liste de courses

4: Vider la liste de courses

5: Quitter le programme

"""

def affichage_liste(liste_de_course):
    for i in range(len(liste_de_course)):
        print(f"{i+1}.  {liste_de_course[i]}")


def menu_liste_de_course():
    print("1: Ajouter un élément à la liste de courses")
    print("2: Retirer un élément de la liste de courses")
    print("3: Afficher les éléments de la liste de courses")
    print("4: Vider la liste de courses")
    print("5: Quitter le programme")

def menu_choix_utilisateur(valeur_choix):
    if valeur_choix.isdigit():
        if int(valeur_choix) in (1, 2, 3, 4, 5):
            return False
        else:
            print("Choix entre 1 et 5 uniquement")
            return True
    else:
        print("Choisir un chiffre numérique entre 1 et 5")
    return True

liste_de_course = []
choix = ""

while choix == "":
    menu_liste_de_course()
    KO = True
    while KO == True:
        choix = input("Votre choix : ")
        KO = menu_choix_utilisateur(choix)

while choix != "5":
    if choix == "3":
        print("-----------------------------------------------------------------------")
        print("Voici la liste de course")
        affichage_liste(liste_de_course)
        # print(liste_de_course)
        print("-----------------------------------------------------------------------")
        menu_liste_de_course()
        KO = True
        while KO == True:
            choix = input("Votre choix : ")
            KO = menu_choix_utilisateur(choix)
    elif choix == "1":
        print("-----------------------------------------------------------------------")
        nouvel_ingredient = input("Saisir un ingrédient : ")
        liste_de_course.append(nouvel_ingredient)
        print(f"L'ingrédient {nouvel_ingredient} a été ajouté à la liste")
        print("-----------------------------------------------------------------------")
        menu_liste_de_course()
        KO = True
        while KO == True:
            choix = input("Votre choix : ")
            KO = menu_choix_utilisateur(choix)
    elif choix == "2":
        suppression_ingredient = input("Ingredient à supprimer : ")
        try:
            print("-----------------------------------------------------------------------")
            liste_de_course.remove(suppression_ingredient)
            print(f"L'ingrédient {suppression_ingredient} a été supprimé")
        except:
            print("L'ingédient n'est pas dans la liste")
        print("-----------------------------------------------------------------------")
        menu_liste_de_course()
        KO = True
        while KO == True:
            choix = input("Votre choix : ")
            KO = menu_choix_utilisateur(choix)
    elif choix == "4":
        print("-----------------------------------------------------------------------")
        liste_de_course.clear()
        print("La liste de course a été supprimé....")
        print("-----------------------------------------------------------------------")
        menu_liste_de_course()
        KO = True
        while KO == True:
            choix = input("Votre choix : ")
            KO = menu_choix_utilisateur(choix)

print("Programme terminé")

