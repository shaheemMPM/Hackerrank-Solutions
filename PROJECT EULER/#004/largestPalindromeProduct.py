# solution get time out
t = int(input())
for i in range(t):
    n = int(input())
    big = 0
    for j in range(100, 1000):
        for k in range(100, 1000):
            num = str(j*k)
            if num == num[::-1] and j*k < n:
                if j*k > big:
                    big = j*k
    print(big)
