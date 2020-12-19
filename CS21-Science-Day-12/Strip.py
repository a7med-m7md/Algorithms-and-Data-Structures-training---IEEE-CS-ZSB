n = int(input())
nums = list(map(int, input().split()))
sumArray = [0]*(n)
sumArray[0] = nums[0]
for i in range(1,n):
    sumArray[i] = sumArray[i-1]+nums[i]

ways = 0

for i in range(n):
    if sumArray[i] == 0 and sumArray[i-1] != 0 :
        ways+=1
print(ways)

## O(N)