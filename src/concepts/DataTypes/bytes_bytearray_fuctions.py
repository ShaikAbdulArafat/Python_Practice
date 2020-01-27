''' bytes is a sequence of numbers ramge from 0 to 256
    *   bytes must be in range(0, 256)
    *   if we use a string for bytes , we'tt get TypeError: 'str' object cannot be interpreted as an integer
    *   So we can't use -ve numbers, float, str or boolean values for a bytes data type.

    *   Byte is a immutable data type, so we can't change its value once it had defined 

    On the other hand 
    
    Bytearray is a sequence of any alphanumeric data 

    *   bytesarray is a mutable data type.
    *   Hence we can change the value of it after its decleration 
'''
lsit1 = [1,0,2,3,5,10,3,4]
bytes1 = bytes(lsit1)
print(type(bytes1))
print(bytes1)       # bytes is immutable

print(max(bytes1))
print(min(bytes1))
print(sorted(bytes1))
print(sorted(bytes1, reverse = True))

bytearray1 = bytearray(b'Hi Python')        
print(type(bytearray1))
bytearray1.append(56)       # bytearray is mutable
print(bytearray1)

print(max(bytearray1))
print(min(bytearray1))
print(sorted(bytearray1,reverse = True))

