# Lektion 0.2, Übung 4: for-Schleife, Summe berechnen
# Berechne mit einer for-Schleife und range(...) die Summe aller Zahlen von 1 bis 100
# (ohne die eingebaute Funktion sum() zu benutzen) und gib das Ergebnis aus.

summe = 0
for i in range(101):
    summe += i
print(summe)
