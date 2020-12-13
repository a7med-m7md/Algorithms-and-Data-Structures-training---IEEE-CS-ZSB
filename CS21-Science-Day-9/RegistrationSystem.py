n = int(input())
names = list()

for i in range(n):
    names.append(input())

printed = dict()

for i in names:
    if i not in printed:
        print("OK")
        printed[i] = 1
    else :
        print(i+str(printed[i]))
        printed[i] = printed[i]+1
        
