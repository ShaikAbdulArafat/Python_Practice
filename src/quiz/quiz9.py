def check_prime(i):
    flag = True
    result =0
    for a in range(2,i):
        if(i % a == 0):
            flag = True
            break
        else :
            flag = False
    if flag:
        pass
    else :
        result = i
    return result

def main(i):
    lt =[]
    for a in range(1,i+1):
        a = check_prime(a)
        if a== 0:
            continue
        lt.append(a)
    # result = [x*len(lt) for x in lt]
    return lt
print(main(11))
