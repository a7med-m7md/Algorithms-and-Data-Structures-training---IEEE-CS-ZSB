n, f = map(int,input().split())
maxAddedItems = []

maxSoldProducts = 0


for i in range(n):
    product, client = map(int, input().split())
    if(f !=0 ):
        if(product > client):
            maxSoldProducts += client
            maxAddedItems.append(0)
        else:
            #product <= client
            maxSoldProducts += product
            if(product != 0 ):
                if(2*product < client):
                    maxAddedItems.append(product)
                else:
                    maxAddedItems.append(client - product)
            else:
                maxAddedItems.append(0)
    else:
        if( product != 0 ):
            if(product > client):
                maxSoldProducts += client
            else:
                maxSoldProducts += product
        else:
            maxSoldProducts += 0

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


mergeSort(maxAddedItems)


for i in range(f):
    maxSoldProducts += maxAddedItems[i]

print(maxSoldProducts)
