avengers = ['hawkeye','ironman','thor','quicksilver']
e = enumerate(avengers)
print(type(e))  #<class 'enumerate'>
print(e)        #<enumerate object at 0x014D5828>
l = list(e)
print(l)    #[(0, 'hawkeye'), (1, 'ironman'), (2, 'thor'), (3, 'quicksilver')]

for a,b, in enumerate(avengers):    # 0 hawkeye
    print(a,b)                      # 1 ironman
                                    # 2 thor
                                    # 3 quicksilver

for a,b in e:           # Nothing will be printed here as i not a iterable
    print(a,b)

for a,b in l:                       # 0 hawkeye
    print(a,b)                      # 1 ironman
                                    # 2 thor
                                    # 3 quicksilver

for a,b in enumerate(avengers,start =10):           # 10 hawkeye
    print(a,b)                                      # 11 ironman
                                                    # 12 thor
                                                    # 13 quicksilver

names = ['barton','stark','odinson','maximoff']

z = zip(avengers,names)
print(type(z))                  # <class 'zip'>
print(z)                        # <zip object at 0x01555928>

li = list(z)
print(li)     # [('hawkeye', 'barton'), ('ironman', 'stark'), ('thor', 'odinson'), ('quicksilver', 'maximoff')]

for a,b in z :                              # hawkeye barton
    print (a,b)                             # ironman stark
                                            # thor odinson
                                            # quicksilver maximoff


for a,b in zip(avengers,names):             # hawkeye barton
    print (a,b)                             # ironman stark
                                            # thor odinson
                                            # quicksilver maximoff
for a,b in li:                              # hawkeye barton
    print (a,b)                             # ironman stark
                                            # thor odinson
                                            # quicksilver maximoff

                                       
print(*z)


avengers1 = ('hawkeye', 'iron man', 'thor', 'quicksilver')
names1 = ('barton', 'stark', 'odinson', 'maximoff')

z1 = zip(avengers1, names1)
a , b =zip(*z1)
print(a,b)
print( a == avengers1) # True
print( b == names1) # True

avengers2 = ('hawkeye', 'iron man', 'thor', 'quicksilver')
names2 = ('barton', 'stark', 'odinson', 'maximoff')
z2 = zip(avengers2,names2)
print(*z2)  #('hawkeye', 'barton') ('iron man', 'stark') ('thor', 'odinson') ('quicksilver', 'maximoff')
print(list(z2)) 
""" #[]   ----- Here we can't get any thing as we already used * above for this iterable,
                  We can't get anything further from this obect """
