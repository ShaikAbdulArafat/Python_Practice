list_a = ['India','USA','China']
print(list_a)
list_a.append('Canada')
print(list_a)
del(list_a[2])
print(list_a)
list_a.insert(int(len(list_a)/2),'Australia')
print(list_a)

set_a = {'India','USA','China'}
print(set_a)
set_a.add('Canada')
print(set_a)
set_a.remove('China')
print(set_a)
set_a.add('Australia')
print(set_a)