#!/usr/bin/env python
# coding: utf-8

# ### Effizienzbetrachtungen für 3 Algorithmen zum Finden des ggT

# In[1]:


def ggt_naiv(a,b):
    d = a # wenn a die kleinere Zahl
    if (d > b):
        d = b # wenn b die kleinere Zahl
    while a % d != 0 or b % d != 0: # Abbruchbedingung
        d = d - 1
    return d


# In[2]:


def ggt_sub(a,b):
    while a != b: # Abbruchbedingung Differenz == 0
        if b > a:
            a,b = b,a # a soll der grössere sein
        a = a - b
    return b   


# In[3]:


def ggt_mod(a,b):
    while a % b != 0: # Abbruchbedingung Rest == 0
        if b > a: 
            a,b = b,a
        a = a % b 
    return b


# In[4]:


get_ipython().run_line_magic('timeit', 'ggt_mod(75,27)')


# In[5]:


get_ipython().run_line_magic('timeit', 'ggt_sub(75,27)')


# In[6]:


get_ipython().run_line_magic('timeit', 'ggt_naiv(75,27)')


# Funktion, die uns die Funktionen für verschiedene Eingaben aufruft

# In[7]:


def test_ggt(f,a):
    """
    berechnet den ggT von a und allen Zahlen b = 1, ..., a mit der Funktion f
    """
    for k in range(1,a):
        f(a,k)


# In[8]:


get_ipython().run_line_magic('timeit', '-n 500 -r 3 test_ggt(ggt_naiv, 100)')


# In[9]:


get_ipython().run_line_magic('timeit', '-n 500 -r 3 test_ggt(ggt_sub, 100)')


# In[10]:


get_ipython().run_line_magic('timeit', '-n 500 -r 3 test_ggt(ggt_mod, 100)')


# In[11]:


125/318


# In[12]:


68/125


# In[20]:


25.5/178


# In[ ]:





# ### Noch ein Beispiel: Summe berechnen 
# ### $\sum_{k=1}^n k$

# In[13]:


def sum1(n):
    """
    Summe iterativ
    """
    s = 0 
    for i in range(1, n + 1):
        s += i
    return s


# In[14]:


sum1(5)


# In[15]:


get_ipython().run_line_magic('timeit', 'sum1(100)')


# In[16]:


get_ipython().run_line_magic('timeit', 'sum1(1000)')


# In[17]:


def sum2(n):
    """
    Gaußsche Summenformel
    """
    return n * (n+1) // 2


# In[18]:


get_ipython().run_line_magic('timeit', 'sum2(100)')


# In[19]:


get_ipython().run_line_magic('timeit', 'sum2(1000)')


# In[ ]:





# In[ ]:





# ### Vergleich while und for loop

# In[1]:


def test_while(n):
    i = 0
    while i < n:
        i+=1
    return i


# In[2]:


def test_for(n):
    i = 0
    for k in range(n):
        i+=1
    return i


# In[3]:


get_ipython().run_line_magic('timeit', '-n 1000 -r 5 test_for(100)')


# In[9]:


get_ipython().run_line_magic('timeit', '-n 1000 -r 5 test_while(100)')


# In[ ]:





# In[ ]:





# In[4]:


i = 0        # 1ZE
while i < n: # n:   1ZE
    i += 1   #      2ZE
             # 1ZE: letzter Test i==n 

