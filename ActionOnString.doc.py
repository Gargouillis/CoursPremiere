"""

chaine = "Bonjour".upper()
print(chaine)

chaine2 = "BonJour".lower()
print(chaine2)

chaine3 = "bonjour".capitalize()
print(chaine3)

chaine4 = "bonjour tout le monde".title()
print(chaine4)

chaine5 = "Bonjour Bonjour".replace("jour", "soir")
print(chaine5)

chaine6 = "Bon Jour Bon Jour".replace(" ", "")
print(chaine6)

chaine7 = "  Bonjour  ".replace(" ", "").replace("jour", "soir")
print(chaine7)

chaine8 = "   Bonjour   ".strip()
print(chaine8)

chaine9 = "   Bonjour   ".strip(" ruoj")
print(chaine9)

chaine10 = "1, 2, 3, 4, 5, 6, 7 ".split(", ")
print(chaine10)
print(type(chaine10))

chaine11 = ", ".join(chaine10)
print(chaine11)
print(type(chaine11))

print("9".zfill(3))


for i in range(10):
    print(i)
    print(str(i).zfill(2))

chaine12 = "Bonjour"
print(chaine12.islower())

chaine13 = "Bonjour"
print(chaine13.istitle())

chaine14 = "Bonjour le jour"
print(chaine14.count("jour"))

print(chaine14.count(" jour"))

chaine15 = "image.png"
print(chaine15.endswith("png"))
print(chaine15.endswith("JPG"))
print(chaine15.startswith("imag"))
print(chaine15.startswith("toto")) 




chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine = chaine.split(", ")
chaine_en_ordre = sorted(chaine)
chaine_en_ordre = ", ".join(chaine_en_ordre)

print(chaine_en_ordre)     """

employes = ["Lucien", "Max", "Gerard", "Denis", "Carole"]
print(employes)

# index() permet de connaitre l'indice de l'elt Gerard
entree = employes.index("Gerard")
print(entree)

# count() permet de compter les occurences d'un elt
employes.append("Max")
employes.append("Max")
print(employes)
nombre_de_max = employes.count("Max")
print(nombre_de_max)

# sort() et sorted()
# sort() trie la liste et remplace
# employes.sort()
print(employes)

# alors que sorted() trie une liste mais ne la modifie pas et met le résultat dans une autre liste
liste_trie = sorted(employes)
print(liste_trie)
print(employes)

# reverse() cette fonction permet juste d'inverser la liste, le dernier devient 1er etc...
employes.reverse()
print(employes)

# pop() permet de supprimer un elt de la liste mais à la différence de remove
# pop n'a pas besoin du "nom" de l'elt mais juste de l'index et on peut même récuperer l'elt supprimé
nom = employes.pop(-1)
print(employes)
print(nom)

# clear() pour vider une liste "définitivement"
#employes.clear()
print(employes)

# join() permet de joindre une liste à un caractère ou autre et transforme la liste en string
resultat_join = " - ".join(employes)
print(employes)
print(resultat_join)
print(type(resultat_join))

# autre chose pour imiter pprint
resultat_pprint = "\n".join(employes)
resultat_tabulation = "\t".join(employes)
print(employes)
print(resultat_pprint)
print(resultat_tabulation)

# split()
courses = "Riz, Lait, Viande, Eau, Pate"
# dans ce cas on écrase la chaine courses : courses = courses.split(", ")
# pour pas écraser on crée une nouvelle variable de type liste
nouvelle_liste = courses.split(", ")
print(courses)
print(nouvelle_liste)