# Lektion 0.3, Übung 4: Kombination mit if
# Schreib eine Funktion ist_gerade(zahl), die True zurückgibt, wenn zahl gerade ist, sonst False
# (nutze % wie in Lektion 0.2). Ruf sie mit ein paar Zahlen auf und gib das Ergebnis jeweils aus.

# Funtkion definieren
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

# Funktionsaufruf mit werden und Rückgabewert in Variablen speichern

test_werte = [3,4,5,6]

for t in test_werte:
    abfrage = ist_gerade(t)
    # Ausgabe auf Konsole und Funktionsaufrauf in der printfunktion
    print(f"Ist {t} gerade? {abfrage}")