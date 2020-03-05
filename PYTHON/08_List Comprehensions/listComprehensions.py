x = int(input())
y = int(input())
z = int(input())
n = int(input())
mat = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(k)
            mat.append(temp)
final = []
for i in mat:
    if sum(i) != n:
        final.append(i)
print(final)
