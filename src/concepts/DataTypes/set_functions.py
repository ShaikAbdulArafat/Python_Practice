"""                 Set is 'mutable' data type. Hence we can enhance the data of a list
                        * We can update a set...
                        * Meaning we can add / remove of a set.
                        * set will not work on indexing mechanism
                        * set will randomly show its elements
                        * Set can't opt sorting, If we sort a set the outcome will be a list

                    Set can't have duplicate elements 
                    Set will alow a None (null) value also
"""

set_a = {1}        # Set with a single element without comma will be a set
print(type(set_a))  # <class 'set'>

set_b = {1,}
print(type(set_b))  # set with a single element with comma also is a set

set_creation = {1,'a',-.43,3.04,True,'hello',43,33,5,5,'a'}
print(set_creation) # {1, 33, 'a', 'hello', 5, 43, -0.43, 3.04} Set will not allow duplicates

set_creation.update((25,'d'))   # adding / updating more elements to set (we can't add elements by index)
print(set_creation)

set_creation.update((None,None)) # set will allow a None / null value
print(set_creation)

set_creation.remove(None)   # removing elements from a set (we can't remove elements by index)
print(set_creation)