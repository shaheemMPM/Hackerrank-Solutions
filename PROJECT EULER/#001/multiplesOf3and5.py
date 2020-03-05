def calc(n):
    return (n+n*n)

T = int(input())
for i in range(T):
    n = int(input())
    n -= 1
    noThree = int(n/3)
    noFive = int(n/5)
    noFifteen = int(n/15)
    print((3*calc(noThree)+5*calc(noFive)-15*calc(noFifteen))>>1)
