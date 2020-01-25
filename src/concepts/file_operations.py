f = open ("students.txt")
print(f)
print(f.read())
f.seek(50)
print(f.read(7))

print(f.tell())
print(f.read(4))
print(f.read())

f.seek(0)
for line in f :
    print (line)
f.seek(0)
print(f.readline())
print(f.readline())

f.seek(0)

print(f.readlines())
f.close()
f.seek(0)
