def check_prime(i):
    result = 0
    for a in range (2,i):
        if i%a == 0:
            # print(i, ' is not a prime number')
            break
        else :
            # print(i ,' is a prime number')
            result = i
            break
    return result

def main(i):
    lt =[2]
    for a in range(2,i+1):
        a = check_prime(a)
        if a== 0:
            continue
        lt.append(a)
    print(lt)
main(15)
