myStr = input()
enteredStr = input()
myStr = myStr.split('|')
left = myStr[0]
right = myStr[1]

for i in range(len(enteredStr)):
    if(len(left)<len(right)):
        left = left + enteredStr[i]
    else:
        right = right +enteredStr[i]

if len(left) != len(right) :
    print("Impossible")
else:
    print(left+"|"+right)
