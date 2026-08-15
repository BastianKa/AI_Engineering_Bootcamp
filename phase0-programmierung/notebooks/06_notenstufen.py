# Lektion 0.2, Übung 2: Notenstufen
# Frag nach einer Punktzahl (0-100) und gib mit if/elif/else eine Note aus:
# >=90 -> "Sehr gut", >=75 -> "Gut", >=50 -> "Bestanden", sonst -> "Nicht bestanden"

eingabe = input("Gib einen Wert zwischen 0 und 100 ein: ")
zahl = int(eingabe)

if zahl < 0 or zahl > 100:
    print("Die Zahl liegt nicht zwischen 0 und 100!")
elif zahl >= 90:
    print("Sehr gut")
elif zahl >= 75:
    print("Gut")
elif zahl >= 50:
    print("Bestanden")
else:
    print("Nicht bestanden")
