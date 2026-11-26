map = [["  ","A","B","C","D","E","F","G","H","I","J"],
       ["1 ","#","#","#","#","#","#","#","#","#","#"],
       ["2 ","#","#","#","#","#","#","#","#","#","#"],
       ["3 ","#","#","#","#","#","#","#","#","#","#"],
       ["4 ","#","#","#","#","#","#","#","#","#","#"],
       ["5 ","#","#","#","#","#","#","#","#","#","#"],
       ["6 ","#","#","#","#","#","#","#","#","#","#"],
       ["7 ","#","#","#","#","#","#","#","#","#","#"],
       ["8 ","#","#","#","#","#","#","#","#","#","#"],
       ["9 ","#","#","#","#","#","#","#","#","#","#"],
       ["10","#","#","#","#","#","#","#","#","#","#"]] #matrice faut voir la taille

def update(ligne, colonne, symbole):
    i = int(ligne)
    j = "ABCDEFGHIJ".index(colonne.upper()) + 1  # transforme les lettres des colones en chiffre "C" -> 3
    map[i][j] = symbole #place le symbole du batiment sur la map

def afficher():
    for ligne in map:
        for colonne in ligne:
            print(colonne, end=" ")
        print()

def index_case(ligne, colonne):
    i = int(ligne)
    j = "ABCDEFGHIJ".index(colonne.upper()) + 1
    return i, j

def lire(ligne, colonne):
    i, j = index_case(ligne, colonne)
    return map[i][j]

def effacer(ligne, colonne):
    i, j = index_case(ligne, colonne)
    map[i][j] = "#"