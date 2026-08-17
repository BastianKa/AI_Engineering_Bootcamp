# Lektion 0.4, Übung 2: Liste verändern
# Nimm die Liste aus Übung 1. Füge mit .append() einen weiteren Namen hinzu,
# entferne einen Namen mit .remove() und gib die Liste danach aus.

namen_liste = ["Anna", "Berta", "Peter"]

namen_liste.append("Heinz")
namen_liste.remove("Anna")

for name in namen_liste:
    print(name)