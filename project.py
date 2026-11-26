import math
import random
import build
import sell
import map_update as mu
import pandas as pd

money = 10000
client = 0
date = 1
rng = random.randint(0,100000) #rng pour events aleatoires
game_state = True
builds_possessed = []
batiment = pd.read_csv("buildings.csv")

mu.afficher()

while game_state == True:
  action = int(input("que faire aujourd'hui:\n"))
  if action == 1:
    a,b = build.construire()
    builds_possessed.append(b)
    money -= a
    print(a,b,builds_possessed)

  elif action == 2:
    pass