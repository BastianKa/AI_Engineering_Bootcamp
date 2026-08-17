# Lektion 0.4, Übung 3: Dictionary
# Erstelle ein Dict person mit den Keys "name", "alter", "stadt". Gib alle drei
# Werte einzeln über den Key aus. Ändere danach den Wert von "alter" und gib
# das ganze Dict aus.

person = {"name":"Sam", "alter":20, "stadt":"Berlin"}

for key, wert in person.items():
    print(key, wert)

person["alter"] = 30
print(person)

# Lektion 0.4, Übung 4: Kombination: Liste aus Dicts
# Erstelle eine Liste mit 2–3 Dicts (z. B. mehrere Personen wie in Übung 3).
# Durchlaufe die Liste mit einer for-Schleife und gib für jede Person Name
# und Alter aus.


Max = {"name":"Max", "alter":20, "stadt":"Berlin"}
Merle = {"name":"Merle", "alter":22, "stadt":"Hamburg"}
Steffi = {"name":"Steffi", "alter":25, "stadt":"Aachen"}

personen_liste = [Max, Merle, Steffi]

for personen in personen_liste:
    print(personen["name"], personen["alter"])