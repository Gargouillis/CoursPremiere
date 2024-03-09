# programme qui permet de calculer les termes d'une suite pour un indice donné

u_courant = 2  # u_coutant est l'indice en cours
indice_max = 15

for n in range(1, indice_max + 1):
    print(f"{u_courant} avant calcul")
    u_courant = 3 * u_courant - 2
    n += 1
    print(f"{u_courant} après le calcul")

print("La valeur u15 est {0}", {u_courant})


# programme qui permet d'additionner les n premiers nombres entiers, n est saisi par l'utilisateur

n = int(input("Saisissez un nombre n, je vous calcule la somme de ces n-1er entier : "))
resultat = 0
for i in range(1, n+1):
    resultat += i
    i += 1

print(resultat)


# programme qui permet de multiplier les n premiers nombres entiers, n est saisi par l'utilisateur

n = int(input("Saisissez un nombre n, je vous calcule la multiplication de ces n-1er entier : "))
resultat = 0
if n != 0:
    resultat = 1
    for i in range(1, n+1):
        resultat *= i
else:
    print("La valeur saisie doit être > 0")
print("Résultat : ", resultat)
print("Programme terminé")
