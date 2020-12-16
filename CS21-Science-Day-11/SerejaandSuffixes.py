n, q = list(map(int, input().split()))
nums = list(map(int, input().split()))
queries = list()

visited = [False] * (100001)

numOfDistinctNums = [0]*(n+1)
visited[nums[n-1]] = True 
numOfDistinctNums[n] = 1

for i in range(q):
    queries.append(int(input()))

for i in range(n-1,-1,-1):
    if visited[nums[i]] == False:
        numOfDistinctNums[i] = numOfDistinctNums[i+1] + 1
        visited[nums[i]] = True
    else:
        numOfDistinctNums[i] = numOfDistinctNums[i+1]

for i in queries:
    print(numOfDistinctNums[i-1])
