# Lektion 0.3, Übung 3: Default-Parameter
# Schreib eine Funktion potenz(basis, exponent=2), die basis hoch exponent zurückgibt
# (Tipp: ** ist der Potenz-Operator in Python).
# Ruf sie einmal nur mit basis auf (nutzt den Default 2) und einmal mit beiden Parametern.

# Funktion definieren
def potenz(basis, exponent=2):
    ergebnis = basis**exponent
    return ergebnis

# Einmal nur mit der Basis
# Funktionsaufruf und Werteübergabe, Rückgabewert wird in Variable gespeichert
mein_ergebnis = potenz(4)

# Ausgabe des Wertes in der Variablen
print(mein_ergebnis)

# Einmal mit der Basis und dem Exponenten, dabei wird der Standardwert exponent=2 überschrieben
# Funktionsaufruf und Werteübergabe, Rückgabewert wird in Variable gespeichert
mein_ergebnis = potenz(4,4)

# Ausgabe des Wertes in der Variablen
print(mein_ergebnis)