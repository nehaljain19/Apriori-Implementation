
# coding: utf-8

# In[12]:

import numpy as np
import pandas as pd
trans= {"{I1, I2, I3}":2, "{I1, I2}": 4, "{I2, I3}": 4, "{I1, I3}": 4, "{I1}": 6, "{I2}": 7, "{I3}": 6}


# In[17]:

c1=trans['{I1, I2, I3}']/trans['{I1}']
c2=trans['{I1, I2, I3}']/trans['{I2}']
c3=trans['{I1, I2, I3}']/trans['{I3}']
c4=trans['{I1, I2, I3}']/trans['{I1, I2}']
c5=trans['{I1, I2, I3}']/trans['{I1, I3}']
c6=trans['{I1, I2, I3}']/trans['{I2, I3}']


# In[18]:

print("C1: ", c1)


# In[23]:

print("C2: ", c2)
print("C3: ", c3)
print("C4: ", c4)
print("C5: ", c5)
print("C6: ", c6)


# In[28]:




# In[25]:




# In[ ]:



