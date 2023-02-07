#!/usr/bin/env python
# coding: utf-8

# ### Definition der verschiedenen ggt Funktionen (Algorithmen)


def ggt_naiv(a,b):
    n = 0 # Zähler für Anzahl der Iterationen 
    d = a # wenn a die kleinere Zahl
    if (d > b):
        d = b # wenn a nicht die kleinere Zahl
    while a % d != 0 or b % d != 0: # Abbruchbedingung
        #print(a,b,d)
        d = d - 1
        n = n + 1 
    return d, n


ggt_naiv(75,27)


def ggt_sub(a,b):
    print("ggT(",a,",",b,") durch Subtrahieren:")
    n = 0 # Zähler für Anzahl der Iterationen 
    while a != b: # Abbruchbedingung
        #print(a,b)
        if b > a:
            a,b = b,a # a soll der grössere sein
        a = a - b
        print("Nach Schritt", n, ":")
        print("a:", a, " b:", b)
        n = n + 1
    return b, n    


ggt_sub(75,27)


def ggt_mod(a,b):
    print("ggT(", a, ",", b, ") durch Modulo/Dividieren:")
    n = 0 # Zähler für Anzahl der Iterationen 
    while a % b != 0: # Abbruchbedingung
        if b > a:
            a,b = b,a
        #print (a,b)
        a = a % b
        print("Nach Schritt", n, ":")
        print("a:", a, " b:", b)
        n = n + 1
    return b, n        


ggt_mod(75,27)


def ggt_rek(a,b):
    #print("ggT(", a, ",", b, ") rekursiv:")
    if b == 0:
        return a
    else: 
        return ggt_rek(b, a % b)


"""
# ### Visualisierung der Anzahl der Schritte jeder Funktion
import numpy as np # python Bibliothek für numerische Berechnungen

a = 100 # eine Zahl ist fest 
b_max = 95 # die zweite Zahl nimmt verschiedene Werte an
np.arange(b_max)


# Definition von Arrays für die Speicherung der berechneten ggT Werte der verschiedenen Funktionen
n_naiv = np.zeros(b_max) 
n_sub =  np.zeros(b_max)
n_mod =  np.zeros(b_max) 


for b in np.arange(b_max):
    n_naiv[b]= ggt_naiv(a,b+1)[1]
    n_sub[b] = ggt_sub(a,b+1)[1]
    n_mod[b] = ggt_mod(a,b+1)[1]



#import matplotlib.pyplot as plt # python Bibliothek zum Erstellen von Graphiken
#plt.plot(n_mod, '.')
#plt.plot(n_naiv, '.k',n_sub, 'r.', n_mod, '.b')

# eventuell muessen Sie den plot explizit anzeigen
#plt.show()
"""

