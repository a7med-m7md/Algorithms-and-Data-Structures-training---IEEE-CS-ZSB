def rotateLeft(d, arr):
    counter = 0
    rotArray = list(arr)
    for i in range(d,len(arr)):
        rotArray[counter] = arr[i]
        counter+=1
    for i in range(0,d):
        rotArray[counter] = arr[i]
        counter+=1
    return rotArray
