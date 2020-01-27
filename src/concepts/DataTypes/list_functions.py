"""                 List is 'mutable' data type. Hence we can enhance the data of a list
                        * Like we can append more elements to a list
                        * Can Insert an element to a list
                        * Can remove an element from a list
                        * Can extend the list 
                        * Can clear a list 

                    List can have duplicate elements 
                    List will alow a None (null) value also
"""
list_l = [4]    # List with a single element without comma will be a list
print(type(list_l))

list_l1 = ['a',]    # List with a single element with comma also be treated as a list
print(type(list_l1))


list_creation = []      # Will create an empty list
print (list_creation)   # [] 
list_with_elments = ['a',1,3.10,True,'Hello',1,None,None]   # Creating list with elements
print(list_with_elments)

list_creation.append(('Abdus')) # Adding element at the end of the list
print(list_creation)
list_with_elments.append(100)   # Adding element at the end of the list
print(list_with_elments)

list_creation.insert(1, 'New Element')  # Inserting element to a list by the index
print(list_creation)
list_with_elments.insert(3, 10000)      # Inserting element to a list by the index
print(list_with_elments)

list_creation.remove('Abdus')   # Removing an element by name from a list
print(list_creation)
list_with_elments.remove(3.10)  # Removing an element by name from a list
print(list_with_elments)

del(list_with_elments[2])       # Deleting an element from a list by its index
print(list_with_elments) 

list_with_elments1 = [3,.3,-.4,5,39,10,200,200]

print(max(list_with_elments1))   # Getting maxium value out of no.of elements of the list

print(min(list_with_elments1))   # Getting minimun value out of no.of elements of the list

list_with_elments1.sort()       # Reversing all the elemets of a numerical  list (Ascending Order)
print(list_with_elments1)

list_with_elments1.sort(reverse=True)   # Reversing all the elemets of a numerical list (Descending Order)
print(list_with_elments1)

list_with_elments1.clear()      # Clearing (deleting all elements from) a list 
print(list_with_elments1)