def largestPrimeFactor(largest):
    div = 2
    while div <= int(largest**0.5):
        if largest%div == 0:
            largest /= div
        else:
            div += 1
    return int(largest)

T = int(input())
for j in range(T):
    n = int(input())
    print(largestPrimeFactor(n))
