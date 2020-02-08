''' Dictonary is a mutable data type.
    * Hence we can change the value of dictionary at any time
    * dictionary is a paired collection of key an value
    * dictionary will not allow duplicate keys. Hence keys of a dictionary is a set data type, and we can 
    * dictionary will allow duplicate values. Hence it is a list
'''

dict1 = {4:'john',2:'bob',3:'bill',5:'bob'}
print(dict1)

print(dict1.items())    # will return the set of tuple pairs of dictionay items
print(dict1.keys())     # will return all the keys as a set
print(dict1.values())   # will return a set of all the values

dit2 = {1:'a', 2:'b', 3:'c', 4:'e', 3:'d'}
                        # If we dupliacte the keys the the first key occurence will be overridden with the latest value
print(dit2)             # here the duplicate 3:'c' is replaced with 3:'d'
print(dit2.items())
print(dit2.keys())
print(dit2.values())

for k in dict1 : print(k)   # default the dictionary object will return key if we use a single local variable in the loop
for k,l in dict1.items() : print(k,l)   # we can use 2 variable from the items to loop through.
for k in dict1.keys(): print(k) # we can use keys only to loop through
for k in dict1.values(): print(k)   # we can values also to loop through

dict1[3] = 'josh'
dict1.update({6:'tim', 7:'kim'})
print(dict1.values())
del(dict1[6])
print(dict1)
