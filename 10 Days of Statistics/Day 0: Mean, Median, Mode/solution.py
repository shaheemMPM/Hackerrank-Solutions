from collections import Counter

def most_common(lst):
    data = Counter(lst)
    return max(lst, key=data.get)

n = int(input())
arr = list(map(int, input().split()))
mean = sum(arr)/n
arr.sort()
if n%2 == 0:
    median = (arr[n//2]+arr[(n//2)-1])/2
else:
    median = arr[(n//2)]

print(mean)
print(median)
print(most_common(arr))
