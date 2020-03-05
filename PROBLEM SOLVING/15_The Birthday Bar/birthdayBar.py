n = int(input())
chocolate = list(map(int, input().split()))
d, m = map(int, input().split())
count = 0
for i in range(n-m+1):
    sum = 0
    for j in range(m):
        sum += chocolate[i+j]
    if sum == d:
        count += 1
print(count)
