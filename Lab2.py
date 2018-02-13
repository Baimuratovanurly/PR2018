
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

operations = pd.read_csv('1 - operations.csv')
operations[:5]


# In[ ]:

dataset = pd.read_csv('2 - dataset.csv')
dataset[:5]


# In[ ]:

new_table_1 = pd.merge(operations, dataset, on='client_id')
new_table_1[:5]


# In[ ]:

types = pd.read_csv('3 - types.csv', sep=';')
types[:5]


# In[ ]:

codes = pd.read_csv('4 - codes.csv', sep=';')
codes[:5]


# In[ ]:

new_table_2 = pd.merge(new_table_1, types, on='type')
new_table_2[:5]


# In[ ]:

print("final merged table: ")
final_table = pd.merge(new_table_2, codes, on='code')
final_table[:5]


# In[ ]:

final_table['client_id'].hist(bins=50)
plt.show()


# In[ ]:

final_table['code'].hist(bins=50)
plt.show()


# In[ ]:

final_table['type'].hist(bins=50)
plt.show()


# In[ ]:

final_table['sum'].hist(bins=50)
plt.show()


# In[ ]:

final_table['status'].hist(bins=50)
plt.show()


# In[ ]:



