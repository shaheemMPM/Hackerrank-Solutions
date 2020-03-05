n = int(input())
students = []
marks = []
for i in range(n):
    std = []
    std.append(input())
    mark = float(input())
    marks.append(mark)
    std.append(mark)
    students.append(std)
marks = list(set(marks))
marks.sort()
if len(marks) >= 2:
    mark = marks[1]
else:
    mark = marks[0]
final = []
for i in students:
    if i[1] == mark:
        final.append(i[0])
final.sort()
for i in final:
    print(i)
