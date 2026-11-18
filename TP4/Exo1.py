n = float(input("Vous cherchez la table de multiplication de quel nombre ?"))

for i in range(0,10):
    print(f"{n} * {i} = {round(n * i, 1)}")

