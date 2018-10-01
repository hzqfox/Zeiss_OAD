import math

def primes2(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

numList = [1,2,3,4,5,6,7,8,9]





var = input("dafsaf")
prims = primes2(int(var))
print(*prims, sep='\n')
print(len(prims))



