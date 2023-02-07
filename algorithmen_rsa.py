#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:39:36 2020

@author: marianne
"""

# RSA-Kryptosystem

# 1. Schlüssel erzeugen
from sympy import prime
p, q = prime(50), prime(54)
n = p * q                   # 57479

from sympy import factorint
phi = (p-1) * (q-1)         # 57000 
print(factorint(phi))       # -> {19:1, 2:3, 3:1, 5:3}
e = 7 * 11                  # 77

# Primfaktorzerlegung aus der letzten Sitzung
factorint(4200)


from sympy import mod_inverse
d  = mod_inverse(e, phi)   # 37013


# 2. Nachricht verschlüsseln - Encryption
N = 52134

def crypt(M, k, m):
    """
    """
    return M**k % m

# encrypt
S = crypt(N, e, n)

# 3. Nachricht entschlüsseln - Decryption
D = crypt(S, d, n)
