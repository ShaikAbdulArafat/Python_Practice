class code:
    def main(self,i):
        self.__i = i
        i = input('provide your input :')
        result = i[0].upper()
        for x in range(1,len(i)):
            result = result+i[x].swapcase()
        return result
# i = input('provide your input :')
ba = code()
print(ba.main("PyThoN"))