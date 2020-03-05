n = int(input())
students = []
for i in range(n):
    std = input().split()
    m1 = float(std.pop())
    m2 = float(std.pop())
    m3 = float(std.pop())
    avg = (m1+m2+m3)/3.00
    std.append(avg)
    students.append(std)
name = input()
for i in students:
    if i[0] == name:
        print(format(i[1], '.2f'))
