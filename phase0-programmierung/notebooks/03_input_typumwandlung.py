# Übung 3: input() und Typumwandlung
# Frage mit input() nach dem Geburtsjahr, wandle die Eingabe in eine Zahl um (int()),
# und berechne daraus näherungsweise das aktuelle Alter. Gib das Ergebnis aus.

eingabe = input("In welchem Jahr hast du Geburtstag?")
geburtsjahr = int(eingabe)
alter = 2026 - geburtsjahr

print("Du bist ungefähr", alter, "Jahre alt.")
