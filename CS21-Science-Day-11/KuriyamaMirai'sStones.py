n = int(input())
stones = list(map(int,input().split()))
m = int(input())
queries = list()
orderedStones = list()
for i in stones:
    orderedStones.append(i)
orderedStones.sort()

prefixSum = [0]*(n)
prefixSum[0] = stones[0]
for i in range(1,n):
    prefixSum[i] = prefixSum[i-1] + stones[i] 

def ordinary(s,e):
    if s == 1:
        return prefixSum[e-1]
    return prefixSum[e-1] - prefixSum[s-2]


prefixSumOrder = [0]*(n)
prefixSumOrder[0] = orderedStones[0]
for i in range(1,n):
    prefixSumOrder[i] =  prefixSumOrder[i-1]+ orderedStones[i] 


def ordered(s,e):
    if s == 1:
        return prefixSumOrder[e-1]
    return prefixSumOrder[e-1] - prefixSumOrder[s-2] 

for i in range(m):
    queries.append(list(map(int,input().split())))

for i in queries:
    if i[0] == 1:
        print(ordinary(i[1],i[2]))
    else:
        print(ordered(i[1],i[2]))
