n=int(input())
numbers=list(map(int,input().split()))
ways=0
sumArray = []
sumArray.append(numbers[0])
for i in range(1,n):
    sumArray.append(pre[i-1]+numbers[i])
 
for i in range(n-1):
    if pre[i]==pre[n-1]-pre[i]:
        ways+=1
print(ways)


## O(N)
