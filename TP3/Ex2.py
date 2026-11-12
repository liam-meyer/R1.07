# a)
"""
n = int((input("Saisissez un nombre : ")))
somme = 0
for i in range(0, n+1):
    somme += i

print(somme)
"""
"""
# b)
a = int(input("Saisissez un nombre : "))

while a != 100:
    a = int(input("Saisissez un nombre : "))

print("termine")
"""
# c)
"""
valeur = []
inferieur10= 0
superieur10= 0
superieur15= 0

for i in range(10):
    while True:
        x = int(input(f"Saisissez un nombre {i+1}: "))
        if 0 < x < 20:
            valeur.append(x)
            break
        else:
            print("valeur invalide")

for i in valeur:
    if i < 10:
        inferieur10 += 1
    elif i >= 15:
        superieur15 += 1
    else:
        superieur10 += 1

print(f"Le nombre de valeurs inférieur strictement à 10 : {inferieur10}")
print(f"Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 : {superieur10}")
print(f"Le nombre de valeurs supérieur ou égale à 15 : {superieur15}")
"""
#d)
X = int(input("Saisissez un nombre superieur a 1: "))
Somme = 1
n=0
while Somme <= X:
    Somme += n
    n+=1
print(n-1)
