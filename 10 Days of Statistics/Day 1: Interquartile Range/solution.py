def median(ar):
    n = len(ar)
    if n%2 == 0:
        med = (ar[n//2]+ar[(n//2)-1])/2
    else:
        med = ar[(n//2)]
    return med

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
arr = []
for i in range(n):
    for j in range(F[i]):
        arr.append(X[i])
arr.sort()
n = len(arr)
limit = n//2
q1 = median(arr[:limit])
if n%2 == 1:
    q3 = median(arr[limit+1:])
else:
    q3 = median(arr[limit:])

iqr = float(q3)-float(q1)
print(round(iqr, 1))
