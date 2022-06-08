tableau = [
    {"nom du sort": "Sort de guerrier",
     "Classe": "Guerrier"
     },
    {"nom du sort": "Sort de mage",
     "Classe": "Mage"
     },
    {"nom du sort": "Sort de voleur",
     "Classe": "Voleur"
     }
]
print(f'{tableau}')
for i in range(len(tableau)):
    print(tableau[i]["nom du sort"])
