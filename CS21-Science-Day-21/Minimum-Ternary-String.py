myString = list(input())


for i in range(len(myString)):
    for j in range(i+1, len(myString)):
        if(myString[i] == '1' and myString[j] == '0') :
            myString[i] = '0' 
            myString[j] = '1'
            break
        elif(myString[j] == '2'):
             i = j
             break
           
    for j in range(i+1, len(myString)):
        if(myString[i] == '2' and myString[j] =='1'):
            myString[i] = '1'
            myString[j] = '2'
            break
            
        

print("".join(myString))
