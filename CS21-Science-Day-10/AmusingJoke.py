guest = input().upper()
host = input().upper()
randomLetters = input().upper()

FreLetter = [0]*(26)
foundLetter = [0]*(26)

def createFreqList(name,curList):
    for i in name:
        curList[ord(i)-65] += 1
    
def canItreturn():
    for i in range(26):
        if FreLetter[i] != foundLetter[i]:
            print("NO")
            return
    print("YES")

createFreqList(guest, FreLetter)
createFreqList(host, FreLetter)
createFreqList(randomLetters, foundLetter)
canItreturn()
