#!/usr/bin/env python
# coding: utf-8

# ### Vergleich der Implementierung: iterativ vs. rekursiv

# ### Beispiel 1: 
# größter gemeinsamer Teiler

# In[1]:


def ggt_mod(a,b):
    while a % b != 0:
        if b > a: 
            a,b = b,a
        a = a % b 
    return b


# In[129]:





# In[2]:


def ggt_rek(a,b):
    if b == 0:
        return a
    else:
        return ggt_rek(b, a%b)


# In[3]:


ggt_rek(27,75)


# In[4]:


def ggt_rek(a,b):
    print("Aufruf mit a:%d und b:%d" %(a,b))
    if b == 0:
        return a
    else:
        print("Selbstaufruf mit b: %d a: %d" %(b,a%b))
        return ggt_rek(b, a%b)


# In[6]:


ggt_rek(27,75)


# ### Beispiel 2: 
# Fakultät $n! = \prod_{i=1}^n i = 1 * 2 * 3 * ... * n$

# In[7]:


def fact_iterativ(n):
    f = 1
    while n > 0: # n = 1, f = 1
        f = f * n
        n = n - 1
    return f


# In[8]:


fact_iterativ(5)


# In[9]:


def fact_rek(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rek(n-1)


# In[20]:


fact_rek(0)


# In[10]:


def fact_rek_v(n):
    print('aufgerufen mit %d' %n)
    if n <= 1:
        print ('gebe Startwert 1 zurück')
        return 1
    else:
        print ('ich rufe mich selbst auf mit %d' %(n-1))
        temp = n * fact_rek_v(n-1)
        print ('gebe zurück %d' %temp)
        return temp


# In[13]:


fact_rek_v(4)


# In[ ]:





# ### Motivation Asymptotische Notation:
# all one polynomial $\sum_{k=0}^n x^k = 1 + x + x^2 + x^3 + ... + x^n$

# In[26]:


def aop1(x,n):
    """
    berechnet 'all one polynomial' n-ten Grades 
    """
    s = 0                  # 1 ZE
    for k in range(n+1):   # n+1: 2 ZE
        p = 1              #      1 ZE   
        for i in range(k): #      k: 2 ZE 
            p *= x         #         2 ZE
        s += p             #      2 ZE 
    return s               # 1 ZE


# In[ ]:


def aop2(x,n):
    """
    berechnet 'all one polynomial' n-ten Grades 
    umgeformt nach Horner Schema
    """
    s = 1                  # 1 ZE
    for i in range(n):     # n: 2 ZE
        s *= x             #    2 ZE
        s += 1             #    2 ZE
    return s               # 1 ZE

