"""
Using iterators to load large files into memory :

Loading data in chunks

    There can be too much data to hold in memory
    Solution: load data in chunks!
    Pandas function: read_csv()
    Specify the chunk: chunk_size
"""


# Iterating Over data

import pandas as pd

result = []
for chunk in pd.read_csv('data.csv',chunksize = 1000):    # object created by read_csv is an iterable...
    result.append(sum(chunk['x']))
total = sum(result)
print(total)
    
for chunk in pd.read_csv('test1.csv', chunksize =10):
    print(chunk['Name'],end = 'Rohit')

df = pd.DataFrame({"a": ['as','he','said'], "b": ['we',0,'one'] ,"c":[7,8,9]})
df1 = pd.DataFrame({'a':(1,2,3),'b':(3,4,5),'c':(5,6,7)},index = (1,2,3))
print(df)
print(df1)

import numpy as np

a = np.array([6,4,4,4])
b = np.array([0,3,8,7])
c = np.array([a,b])

print(c.shape)
bool_exp = a > 5
print(bool_exp)
print(np.corrcoef(a,b))

x=1
print(bool(x))