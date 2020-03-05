def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primeLessThan(n):
    primeless = []
    for i in range(2, n+1):
        if isPrime(i):
            primeless.append(i)
    return(primeless)

def powerLess(num, limit):
    i = 1
    while(num**i <= n):
        i += 1
    return i-1

t = int(input())
for i in range(t):
    n = int(input())
    primeless = primeLessThan(n)
    powers = []
    for j in primeless:
        powers.append(powerLess(j, n))
    res = 1
    for j in range(len(powers)):
        res *= (primeless[j]**powers[j])
    print(res)
