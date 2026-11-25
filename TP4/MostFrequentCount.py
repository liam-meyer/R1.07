L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

n = L1[0]
compteur = 0
Max = 0

for i in L1:
    compteur = L1.count(i)
    if compteur > Max:
        Max = compteur
        n = i

print(f"Le nombre le plus frequent dans la liste est le : {n} ({Max} x)")


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""