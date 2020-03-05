lineF = list(map(int, input().split()))
lineS = list(map(int, input().split()))
lineT = list(map(int, input().split()))
sumF = sum(lineF)
sumS = sum(lineS)
sumT = sum(lineT)
res = abs(15-sumF)+abs(15-sumS)+abs(15-sumT)
print(res)
#logic not ok
