#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# sort weight
weight = [4, 4, 2, 1, 6, 3]
capacity = 20
profit = [6, 7, 4, 3, 9, 5]

dataset = pd.DataFrame({"weight": weight,
                       "profit": profit})
dataset


# In[25]:



density = [a/b for a, b in zip(profit, weight)]
dataset["density"] = density
dataset_sort = dataset.sort_values(by=["density", "profit"],
                                  ascending=False)
dataset_sort.reset_index(inplace=True)
dataset_sort


# In[37]:


knapsack_i = []
knapsack_v = 0
knapsack_w = 0

for i in range(len(dataset_sort)):
    if (knapsack_w + dataset_sort["weight"][i]) <= capacity:
        knapsack_i.append(dataset_sort["index"][i])
        knapsack_v = knapsack_v + dataset_sort["profit"][i]
        knapsack_w = knapsack_w + dataset_sort["weight"][i]

print("item", knapsack_i)
print("value", knapsack_v)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


# In[35]:


dy_table = pd.DataFrame(np.zeros((capacity+1, len(weight)+1)))

dy_table.iloc[weight[0]:, 1] = profit[0]
dy_table.iloc[weight[0]:weight[1], 2] = profit[0]

for i in range(1, len(weight)):
    dy_table.iloc[:weight[i], i+1] = dy_table.iloc[:weight[i], i]
    for j in range(weight[i], capacity+1):
        add_i = dy_table.iloc[j-weight[i], i]+profit[i]
        not_add_i = dy_table.iloc[j, i]
        if add_i >= not_add_i:
            dy_table.iloc[j, i+1] = add_i
        else:
            dy_table.iloc[j, i+1] = not_add_i
dy_table


# In[36]:


item = []
j = capacity
for i in range(len(weight), 0, -1):
    if dy_table.iloc[j, i-1] != dy_table.iloc[j, i]:
        item.append(i-1)
        j = j - weight[i-1]
print("item", item)
print("profit", dy_table.iloc[-1, -1])
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


# In[ ]:




