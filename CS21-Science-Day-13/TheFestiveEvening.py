n, g = list(map(int, input().split()))
intrances = input().upper()
numsIntrances = dict()
nonRepeated = set()

for i in range(n):
    numsIntrances[intrances[i]] = i

for i in range(n):
    nonRepeated.add(intrances[i])
    if(len(nonRepeated)>g):
        print("YES")
        break
    if i == numsIntrances[intrances[i]]:
        nonRepeated.remove(intrances[i])
if len(nonRepeated) <= g:
    print("NO")
