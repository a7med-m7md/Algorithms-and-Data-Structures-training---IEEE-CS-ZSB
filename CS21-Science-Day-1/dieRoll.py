scan = input().split()
Yakko = int(scan[0])
Wakko = int(scan[1])

picked = Yakko if Yakko>=Wakko  else Wakko
a = (6-picked)+1
b = 6
if picked == 1:
    print(str(1)+"/"+"1")
elif a==3 :
    print("1/2")
elif a%2 == 0:
    a//=2
    b//=2
    print(str(a)+"/"+str(b))
else:
    print(str(a)+"/"+str(b))
