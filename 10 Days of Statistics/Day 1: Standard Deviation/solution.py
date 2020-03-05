n = int(input())
arr = list(map(int, input().split()))
mean = sum(arr)/n
sigma = 0
for i in arr:
    temp = mean-i
    temp *= temp
    sigma += temp
sigma /= n
sigma = sigma**0.5
sigma = round(sigma, 1)
print(sigma)
