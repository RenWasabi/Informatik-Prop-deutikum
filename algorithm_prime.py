#!/usr/bin/env python
# coding: utf-8


import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    for i in np.arange(2,n):
        if n % i == 0:
            return False
    return True


# probieren Sie die Funktion aus für eine beliebige Zahl
is_prime(131)


def is_prime2(n):
    if n <= 1:
        return False
    for i in np.arange(2, 1+np.int(np.sqrt(n))): # np.arange(2,n) max=(n-1) 
        if n % i == 0:
            return False
    return True

# probieren Sie die Funktion aus für eine beliebige Zahl


# Erzeugen einer Liste der ersten 30 Primzahlen
L = []
n = 2
while len(L) < 30:
    if is_prime(n):
        L.append(n)
    n = n + 1

L
# list comprehension in python - effiziente Art, sich Liste zu erzeugen
t = [b**2 for b in np.arange(10)]

# konvertiere Liste in numpy array
np.array(L)

# Graphischer Vergleich der Effizienz der beiden Algorithmen
# Anzahl der Schleifendurchläufe gegeneinander abtragen
import matplotlib.pyplot as plt

x = L
y_p = [k-2 for k in L] 
y_p2= [np.int(np.sqrt(k))-1 for k in L]

plt.plot(x,y_p)
# eventuell muessen Sie den plot explizit anzeigen
plt.show()

# '.r' - letztes Argument - style für plot
plt.plot(L, y_p, '.b', L, y_p2, 'r.')

# eventuell muessen Sie den plot explizit anzeigen
plt.show()

# Sieb des Eratosthenes
def sieb(n):
    primzahlen = []  # leeres Listenobjekt, damit wir remove Methode anwenden können s.u.
    zahlen = list(range(2, n+1)) # erzeugt Liste der Ausgangszahlen von 2 bis n
    c = 2            # kleinste Primzahl
    while c * c < n: # solange c kleiner ist als Wurzel(n)
        for k in np.arange(c, (n+1), c): # Vielfache der Siebzahl c in den Ausgangszahlen
            if k in zahlen:              # wenn ein Vielfaches von c in den Ausgangszahlen ist 
                zahlen.remove(k)         # entferne diese Zahl aus der Liste
        primzahlen.append(c)             # hänge c selbst an die Liste der Primzahlen
        c = zahlen[0]                    # neue Siebzahl wird die aktuell kleinste Zahl in den Ausgangszahlen
    return primzahlen + zahlen           # Primzahlen, sind die Siebzahlen bis Wurzel(n) plus alle übrigen
    


# probieren Sie die Funktion aus für eine beliebige Zahl

p = sieb(11)
print(p)
