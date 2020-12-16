n = int(input())
colors = input().lower()

colorsFreq = [0] * 26
def check():
    for i in colors:
        colorsFreq[int(ord(i))-97] += 1
        if colorsFreq[int(ord(i))-97] > 1:
            print("YES")
            return
    print("NO")
if n != 1:
    check()
else:
    print("YES")