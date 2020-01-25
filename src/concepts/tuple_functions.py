"""                 Tuple is an 'Immutable' data type. Hence we can't enhance the data of a tuple
                        * Like we can't append more elements to a tuple
                        * Can't Insert an element to a tuple
                        * Can't remove an element from a tuple
                        * Can't extend the tuple 
                        * Can't clear a tuple 
                    
                    Mostly we just can access the data of a tuple
                    Tuple can have duplicate values
                    Tuple can have None (null) value 
                    
            If we have to define a tuple with single element we should use comma (,) at the end of the value
"""

tuple_creation = ()
print(tuple_creation)
print(type(tuple_creation))     # <class 'tuple'>

tuple_a = ('a')       # Tuple with a single element without comma is not a tuple
tuple_a1 = ('a',)     # Tuple with a single element with a comma is treated as a tuple
print(type(tuple_a))    # <class 'str'>
print(type(tuple_a1))   # <class 'tuple'>

tuple_b = (1)
tuple_b1 = (1,)
print(type(tuple_b))    # <class 'int'>
print(type(tuple_b1))    # <class 'tuple'>

tuple_c = (True)
tuple_c1 = (True,)
print(type(tuple_c))    # <class 'bool'>
print(type(tuple_c1))    # <class 'tuple'>

tuple_new = (0,1,.1,1.5,True,'hi',None,None,1)
print(tuple_new)