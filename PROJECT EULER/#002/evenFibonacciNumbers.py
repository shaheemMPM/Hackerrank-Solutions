def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        li = [1, 2]
        while 1:
            temp = li[-1]+li[-2]
            if temp <= n:
                li.append(temp)
            else:
                break
        return li

T = int(input())
for j in range(T):
    n = int(input())
    lis = []
    for i in fibonacci(n):
        if i%2 == 0:
            lis.append(i)

    print(sum(lis))
