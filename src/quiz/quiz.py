from distutils.filelist import findall
def diff(a,b):
    for x in b:
        while x in a:
            a.remove(x)
    return a
            
print(diff([], [1,2]))
# print(dir(list))