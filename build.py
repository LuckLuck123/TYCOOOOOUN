import pandas as pd
import map_update as mu

builds = pd.read_csv("buildings.csv")
infos = builds.set_index("initiale").to_dict("index")

def construire():
    print(builds)
    b = int(input("quoi construire "))
    batiment = builds.iloc[b]
    print(batiment)
    placement = input("position? (chiffre puis lettre, ex: 3C) ")
    mu.update(placement[:-1], placement[-1], batiment["initiale"])
    mu.afficher()
    price = batiment["price"]
    name = batiment["initiale"]
    return price, name



if __name__ == "__main__":
    a,b =construire()
    print(a,b)