def median(ar):
    n = len(ar)
    if n%2 == 0:
        med = (ar[n//2]+ar[(n//2)-1])/2
    else:
        med = ar[(n//2)]
    return med

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
q2 = median(arr)
limit = n//2
q1 = median(arr[:limit])
if n%2 == 1:
    q3 = median(arr[limit+1:])
else:
    q3 = median(arr[limit:])
print(int(q1))
print(int(q2))
print(int(q3))
