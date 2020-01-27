"""         A first fundamental distinction that Python makes on data is about whether or not the value of an object changes. 
            If the value can change, the object is called mutable, while if the value cannot change, the object is called immutable.

                    *********   Mutable Data Types    *************

                            1. list
                            2. bytearray
                            3. set
                            5. dictionaries
"""

#       Every object in Python has an ID (or identity), a type, and a value

'''(1) List ''' # list data type is a mutable data type

list_a = [10,20,30]
print('id of th list object is : ',id(list_a))  # Once id is created, The id of an object never changes. It is unique..
print(type(list_a))    # The type also never changes. It tells what operations are supported by the object. 
                    # And the possible values that can be assigned to it.

print(list_a)      # The value can either cahnge or not. If it can change it is said to be mutable,
                    # While it can't, The value is said to be immutable

list_a.pop()
print(list_a)
print('id of the list ofter changing its value is : ',id(list_a))

list_a.append('hero')
print(list_a)
print('id of the list object after changing its value again is : ',id(list_a))


'''(2) ByteArray ''' # bytes data type is a mutable data type

bytearray_a = bytearray(b'ByteArrray')
print(type(bytearray_a))
print('id of the bytearray data type is : ',id(bytearray_a))
print(bytearray_a)


bytearray_a.reverse()
print(bytearray_a)
print('id of bytearray after changing its value is : ',id(bytearray_a) )

'''(3) Set ''' # set data type is a mutable data type

set_a = {'a','b'}
set_b = set(('a','b'))
print(type(set_a))
print('id of set - a datatype is : ',id(set_a))
print(set_a)
set_a.add('c')
print('id of set - a data type after changing its value is : ',id(set_a))
print(set_a)

print(type(set_b))
print('id of set - b data type is : ',id(set_b))
print(set_b)
set_b.discard('a')
print("id of set - b  data type after changing it's value is : ",id(set_b))
print(set_b)


'''(4) Dictionaries ''' # dict data type is a mutable data type

dict_a = {'a':'alpha','b':'beta','c':'gamma'}

print(type(dict_a))
print('id of dict data type is : ', id(dict_a))
print(dict_a)

dict_a.update({'d':'bella'})
print('id of dict data type after changing its value is : ', id(dict_a))
print(dict_a)