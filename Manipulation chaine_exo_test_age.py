# Les fonctions
"""
nom = "toto"
print("Je m'appelle " + nom)    # ici on fait une concaténation, donc on passe 1 seul paramètre à print()
                                # c''est à dire la chaine de caractères concaténées

print()                         # ici on ne passe pas de paramètre

print("Je m'appelle", nom)      # ici on passe 2 paramètres, une chaine de carctères et une variable

print("Je m'appelle", nom, "j'ai", 30, "ans")  # ici on passe 5 paramètres
"""

def est_majeur(age):
    return age >= 18

"""
recuperer_et_afficher_infos_personne()
    -> recuperer_infos_personne()
    -> afficher_infos_personne()
        -> est_majeur()
"""
    
def recuperer_infos_personne(numero_personne):
    nom = input(f"Nom de la personne {numero_personne} ? ")
    age = int(input("Votre age? "))
    return nom, age


def afficher_infos_personne(numero_personne, nom, age):
    bool = est_majeur(age)
    if bool == True:
        majorite = "Majeur"
    else:
        majorite = "Mineur"
    if age != 0:
        print(f"Le nom de la personne {numero_personne} {nom} a {age} ans et tu es {majorite}")
    else:
        print(f"Le nom de la personne {numero_personne} {nom}")

    print("Longeur de votre prénom", len(nom))


for i in range(0, 2):
    nom, age = recuperer_infos_personne(i+1)
    afficher_infos_personne(i + 1, nom, age)

"""
# implementer recuperer_et_afficher_infos_personne
# parametre = numero de la personne
# rien retourner
# input / print
def recuperer_et_afficher_infos_personne(numero_personne):
    nom = input(f"Nom de la personne {numero_personne} ? ")
    age = int(input("Votre age? "))

    if age != 0:
        print(f"Le nom de la personne {numero_personne} {nom} a {age} ans")
    else:
        print(f"Le nom de la personne {numero_personne} {nom}")

    print("Longeur de votre prénom", len(nom))


NB_PERSONNES = 3

for i in range(NB_PERSONNES):
    recuperer_et_afficher_infos_personne(i+1)




def est_majeur(age):
    return age >= 18



# definition de la fonction
def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas de nom, l'age vaut", age)
    else:
        if age == 0:
            print("Mon nom est " +  nom)
        else:
            print("Mon nom est " + nom, "j'ai" , age, "ans")
        print("Mon nom comporte", len(nom), "lettres")

print("Debut du programme ")

afficher_infos_personne(age = 10)
print("Fin du programme ")

print(est_majeur(159))"""
