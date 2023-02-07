#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Geburtstagsparadoxon


def P (k):
    """
    Anzahl der günstigen geteilt durch Anzahl der möglichen
    k - abhängig von der Anzahl der Personen
    n! / (n-k)! = n * (n -1) * ... * (n - k + 1)
    """
    n_moeglich = np.float(365**k)
    prod = 1
    for i in range(k):
        prod = prod * (365 - i)
    return (n_moeglich - prod ) / n_moeglich



P(20)

P(22)

P(46)

# Bedingte Wahrscheinlichkeit


from itertools import product
## kartesisches Produkt

list(product(["A","B"], {1,2,3}))


x = np.arange(1,7)
x

6**3
omega = list ( product (x,x,x))
len(omega)


## lambda function & filtering 
## filter(function, iterable) 
## -> iterator contains only elements from iterable for which function returns True

## Beispiel: alle Zahlen, die durch 3 teilbar sind, aus der Liste der Zahlen von 2 bis 18 rausfiltern
## Funktion returns TRUE and FALSE, filter gibt nur die Elemente der Liste aus für die die Funktion TRUE ist


def mod3(x):
    """
    returns 1 if division by 3 has remainder 0
    """
    return x % 3 ==0


first_even=np.arange(2,20,2)
first_even[[mod3(x) for x in range(2,20,2)]]


t = lambda x: x % 3 == 0
t(17)

list ( filter ( lambda x:  x % 3 ==0,  range(2,20,2)) ) 


list(filter(mod3, range(2,20,2)))

## set -> Menge 

set(omega[1])


P = lambda test: len(list(filter(test, omega)))

## Ereignismengen
P( lambda L: sum(L) <= 9 )
P(lambda L: len(set(L)) < 3)



def P (test, omega):
    """
    definiere mir Filter, die ich auf Omega anwende
    test - ist Funktion oder Bedingung
    """
    return len ( list ( filter( test, omega) ))





P(lambda L: sum(L) <= 9, omega)/ 6.**3
P(lambda L: len(set(L)) < 3, omega )/ 6.**3



## veränderte Ergebnismenge Omega erzeugen
omega1 =  list (filter (lambda L: 1 in L, omega ))

len(omega1)


P(lambda L: sum(L) <= 9, omega1)
P(lambda L: len(set(L)) < 3, omega1)
P(lambda L: len(set(L)) < 3, omega1)/np.float(len(omega1))
