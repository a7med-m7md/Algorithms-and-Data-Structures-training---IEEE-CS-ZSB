n = int(input())
inputString = input().lower()
freList = [0] * (26)


def checkPangram(inputStr):
    for i in inputStr:
        freList[ord(i)-97]+=1

checkPangram(inputString)

if 0 not in freList:
    print("YES")
else:
    print("NO") 
# T = O(n)