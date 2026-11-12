import random

x = random.randint(0,100)
n = int(input("Entrez un nombre : "))
compteur = 1
while n != x:

    if n < x:
        print("La valeur a trouver est plus grande")
    else:
        print("La valeur a trouver est plus petite")

    n = int(input("Entrez un nombre : "))
    compteur += 1

print(f"Trouve en {compteur} tours ! ")