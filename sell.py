import map_update as mu
from build import infos

POURCENTAGE_REMBOURSEMENT = 0.6   # 60 % du prix d'achat rendu en vente

def sell(placement, possedes, money):
    """Vend le bâtiment situé à `placement` (ex: "3C").
    Retourne le nouvel argent."""
    ligne, colonne = placement[:-1], placement[-1]

    try:
        initiale = mu.lire(ligne, colonne)
    except (ValueError, IndexError):
        print("Position invalide")
        return money

    if initiale == "#":
        print("Il n'y a rien à vendre ici")
        return money

    possedes.remove(initiale)        # retire une occurrence de la liste
    mu.effacer(ligne, colonne)       # remet "#" sur la map
    remboursement = int(infos[initiale]["price"] * POURCENTAGE_REMBOURSEMENT)
    print(f"{infos[initiale]['name']} vendu pour {remboursement}")
    return money + remboursement
