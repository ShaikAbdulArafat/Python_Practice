"""         A first fundamental distinction that Python makes on data is about whether or not the value of an object changes. 
            If the value can change, the object is called mutable, while if the value cannot change, the object is called immutable.

                    *********   Immutable Data Types    *************

                            1. int
                            2. str
                            3. tuple
                            4. 


"""

#       Every object in Python has an ID (or identity), a type, and a value

'''(1) Interger ''' # Int data type is an Immutable data type

age = 42
print('id of the first age object : ', id(age))  # Once id is created, The id of an object never changes. It is unique..
print(type(age))    # The type also never changes. It tells what operations are supported by the object. 
                    # And the possible values that can be assigned to it.
print(age)      # The value can either cahnge or not. If it can change it is said to be mutable,
                # While it can't, The value is said to be immutable

age = 43
print('id of the age when the value is chagned : ', id(age)) # The Id of age object is not the same.. It is a new object


'''(2) String ''' # str data type is an Immutable data type

name = 'Hella'
print('id of the name object is : ',id(name))
print(name)

name = 'Bella'
print('id of name object when its value is changed : ',id(name))
print(name)
