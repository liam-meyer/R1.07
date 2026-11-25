nMax = 10
v1 = []
v2 = []
scalaire = 0

n = int(input(f"Quelle est la taille de vos vecteurs entre 1 et  {nMax} ? "))
print()

while n < 1 or n > nMax:
    n = int(input(f"Quelle est la taille de vos vecteurs entre 1 et  {nMax} ? "))

print("Saisie du premier vecteur : ")
for i in range(0, n):
    v1.append(float(input(f"v1[{i}] =  ")))

print()


print("Saisie du second vecteur : ")
for i in range(0, n):
    v2.append(float(input(f"v2[{i}] =  ")))

print()

for i in range(0, n):
    scalaire += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {scalaire}")