def main(i):
    b = []
    for a in i:
        a = list(a)
        a.sort()
        a.reverse()
        b.append(a[0]-a[1])
    result = b[0]
    count = 0
    for a in range(1,len(b)):
        if b[count] < b[a] :
            result = b[a]
        else:
            result = b[count]
        count=count+1
    print (result)

# main([(10,12),(8,15),(20,8),(2,-10),(1,12),(-23,1),(32,34)])

i=[(10,12),(8,15),(20,8),(2,-10),(1,12),(-23,1),(32,34)]
def mains(i):
    b =[]
    for a in i :
        a = list(a)
        result =0
        if a[0] > a[1]:
            result = a[0]-a[1] 
        else :
            result = a[1]-a[0]
        b.append(result)
    print(b)
    result = b[0]
    count = 0
    for a in range(1,len(b)):
        if b[count] < b[a] :
            result = b[a]
        else:
            result = b[count]
        count=count+1
    print (result)
# print(dir(tuple))
mains(i)
    

