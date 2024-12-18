import os

file = open("./Day 1/1.txt", "r")

col1 = []
col2 = []
for line in file.readlines():
    col1.append(int(line.split("   ")[0]))
    col2.append(int(line.split("   ")[1]))

col1.sort()
col2.sort()

res = 0
for a, b in zip(col1, col2):
    if a > b:
        res += (a-b)
    else:
        res += (b-a)
        pass
# sol1
print(res)

set1 = set(col1)
set2 = set(col2)

c = {key: 0 for key in set2}
for a in col2:
    c[a] += 1

res2 = 0
for a in set1:
    if a in c:
        res2 += a*c[a]

print(res2)
