n = int(input())
data = list(map(int, input().split()))
weight = list(map(int, input().split()))

w_data = []
for i in range(n):
    w_data.append(data[i]*weight[i])
mean = sum(w_data)/sum(weight)
print(round(mean, 1))
