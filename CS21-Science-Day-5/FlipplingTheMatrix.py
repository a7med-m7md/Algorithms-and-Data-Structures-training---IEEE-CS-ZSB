q = int(input())
n = int(input())

matrix = []
for i in range(2*n):
    row = list(map(int,input().split()))
    matrix.append(row)

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s
    
print(flippingMatrix(matrix))