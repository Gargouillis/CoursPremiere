# I will, in this project, group all followed training from Udemy for example


def saisie_indice():
    index = int(input("Saisir un indice : "))
    return index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    indice_1 = saisie_indice()
    u1 = 1/2
    for i in range(1, indice_1):
        i += 1
        suite_n = u1 + (1/(i*(i+1)))
        print(suite_n)
    print("Le résultat est ", suite_n)



