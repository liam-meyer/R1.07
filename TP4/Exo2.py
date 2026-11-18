nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

notes = []

for i in range(0, nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        note = float(input(f"Note etudiant entre 0 et 20 stp {i} : "))
    notes.append(note)
    moyenne += note

moyenne = moyenne/nombreEtudiants
print(f"Moyenne de classe : {moyenne}" )
print("Numero de l’Etudiant | note | ecart a la moyenne ")

for i in range(0, nombreEtudiants):
    print(f"{i} | {notes[i]} | {moyenne-notes[i]}")
