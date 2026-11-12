n = int(input("Entrez un nombre : "))
factorielle = 1

choix = str(input("Quelle type de boucle: for ou while"))

while choix not in "forwhile"
"""
for i in range(1, n+1):
    factorielle *= i
    print(i)
    print(factorielle)
"""

while n > 0:
    factorielle *= n
    print(n)
    n -= 1
print(factorielle)