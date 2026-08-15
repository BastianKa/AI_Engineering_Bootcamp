# Lektion 0.2, Übung 3: while-Countdown
# Schreib eine while-Schleife, die von 10 runterzählt bis 1 (jede Zahl in einer eigenen Zeile),
# und am Ende "Start!" ausgibt.

zahl = 10
zahl = int(zahl)
while zahl > 0:
    print(zahl)
    zahl = zahl - 1
else:
    print("Start!")