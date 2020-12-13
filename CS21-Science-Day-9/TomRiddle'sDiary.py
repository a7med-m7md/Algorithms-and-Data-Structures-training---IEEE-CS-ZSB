n = int(input())
names = list()
printed = list()
for i in range(n):
    names.append(input())

for i in names:
    if i not in printed:
        printed.append(i)
        print("NO")
    else:
        print("YES")