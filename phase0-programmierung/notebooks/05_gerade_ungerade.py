# Lektion 0.2, Übung 1: Gerade oder ungerade
# Frag mit input() nach einer Zahl, wandle sie in int um, und gib mit if/else aus,
# ob sie gerade oder ungerade ist. Tipp: zahl % 2 == 0 → gerade.

eingabe = input("Gib eine zahl ein: ")
zahl = int(eingabe)
if zahl % 2 == 0:
    print(f"{zahl} ist eine GERADE Zahl.")
else:
    print(f"{zahl} ist eine UNGERADE Zahl.")