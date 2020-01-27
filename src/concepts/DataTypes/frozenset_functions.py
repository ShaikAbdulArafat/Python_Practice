"""                 frozenset is 'immutable' data type. Hence we can't enhance the data of a frozenset
                        * Like we can't append more elements to a frozenset
                        * Can't Insert an element to a frozenset
                        * Can't remove an element from a frozenset
                        * Can't extend the frozenset 
                        * Can't clear a frozenset
                    frozenset can be created from a set
                    frozenset can't have duplicate elements 
                    frozenset will alow a None (null) value also

        Only operation that can be performed on a frozenset is loop over a frozenset and retrive its elemets
"""
set_creation = {1, 33, 5, 43, None, -0.43, 'a', 3.04, 25, 'hello', 'd',None}
set_creation1 = { 1,2,34,3,37,3,7,233,7832,7,.78,-.45,34.45,-35.434}

frozenset_creation = frozenset(set_creation)

print(frozenset_creation)
print(type(frozenset_creation))

print(len(frozenset_creation))

frozenset_creation1 = frozenset(set_creation1)
f = sorted(frozenset_creation1)
print(f)

f = sorted(frozenset_creation1, reverse = True)
print(f)

"""     We can use all default python methods which doesn't modify the values of a frozenset
        Like we can use max ,min functions 
        we can use len function
        we can sort a frozenset for ascending order , for decsnding order we can use reverse=True 
"""