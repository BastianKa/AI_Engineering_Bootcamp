# Lektion 0.3, Übung 2: Funktion mit Rückgabewert
# Schreib eine Funktion addiere(a, b), die die Summe zurückgibt (return, nicht print).
# Speichere das Ergebnis in einer Variable und gib die Variable danach mit print aus.

# Funktion definieren
def addiere(a,b):
    summe = a + b
    return summe

# Funktion aufraufen und Werte übergeben, Rückgabewert in Variable speichern
meine_summe = addiere(2,5)

# Wert der Variablen ausgeben
print(meine_summe)