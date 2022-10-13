def taille(liste):
    taille_liste = []
    #On pracoure chaque mot de la liste et ajoute la longeure du mot a une liste
    for mot in liste:
        taille_liste.append(len(mot))
    return taille_liste

def lire(n):
    liste = list()
    #On fait n demande de mot et l'ajoute a la liste
    for i in range(n):
        mot = input("Tapez un mot : ")
        liste.append(mot)
    return liste

def affiche(liste):
    taille_mot = taille(liste)
    moyenne = 0
    mots_plus_long = str()
    for i in range(len(liste)): #parcours chaque indice de la liste et affiche le mot ainsi ainsi que sa taille et calcul le total de caractères
        print(f"Taille du mot {liste[i]} : {taille_mot[i]}")
        moyenne += taille_mot[i]
    moyenne = moyenne/len(liste)
    for i in range(len(liste)):#parcours chaque indice de la liste pour trouver les mots plus long que la moyenne
        if taille_mot[i] >= moyenne:#si la taille du mot est supérieur à celle de la moyenne, on l'ajoute à la liste
            mots_plus_long += liste[i]
    return f"Taille moyenne: {moyenne}\nMots plus longs que la moyenne: {mots_plus_long}"

def nbocc(mot,carac):
    occurences = 0
    for lettre in mot: # parcours chaque lettre du mot et compte si la lettre est celle recherché
        if lettre == carac:
            occurences+=1
    return occurences

def compteCarac(liste,car):
    mots_avec_car = list()
    occurence_total = 0
    chaine = str()
    for mot in liste: #parcours les mots de la liste et si le caractère est trouvé dans celui ci, alors il est rajouté à la liste de mot contenant le caractère et compte le nombrre d'occurence total.
        occurence = nbocc(mot,car)
        if occurence >= 1: 
            mots_avec_car.append(mot)
            occurence_total+=occurence
    if len(mots_avec_car) > 0: #Si il y a un mot avec le caractère cherché, affiche le nombre de mot contenant le caractère, chacun de ces mots et le nombre d'occurence total.
        chaine+= f"Mots contenant le caractère {car}\n"
        for mot in mots_avec_car: 
            chaine+= mot+ "\n"
        chaine+=f"Le caracère {car} apparait {occurence_total} fois."
    else:
        chaine+= f"Erreur la lettre {car} n'est présente dans aucun des mots"

def temp(liste,car):
    occurence_max = 0
    mot_max = str()
    for mot in liste: #parcours chaque mot de la liste et stock le mot avec le plus grand nombre d'occurence (si il y en a plusieurs garde le plus petit mot)
        occurence = nbocc(mot,car)
        if occurence > occurence_max:
            occurence_max = occurence
            mot_max = mot
        elif occurence == occurence_max:
            if len(mot) < len(mot_max):
                occurence_max = occurence
                mot_max = mot
    if occurence_max > 0: 
        return f"Mot avec le plus de recurence: {mot_max}\nNombre d'occurence dans ce mot: {occurence_max}"
    return f"Erreur la lettre {car} n'est présente dans aucun des mots"

nombre_de_mots = int(input("Nombre de mots a ecrire: "))
mots = lire(nombre_de_mots)
taille_mots = taille(mots)
for i in range(len(mots)):
    print(f"{mots[i]} est de longueur {taille_mots[i]}")
joue = True
while joue: #demande à l'utilisateur un caractère jusqu'à que celui-ci ne veut plus jouer
    caractere = input("Entrez un caractere: ")
    print(temp(mots,caractere))
    Rejouer = input("Rejouer ? ")
    if rejouer == "non":
        joue = False