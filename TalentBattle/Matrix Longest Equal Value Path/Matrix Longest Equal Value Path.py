directions = [[1, 1], [1, -1], [1, 0], [0, 1]]


def consecutivePath(matrix):
    arr = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if(check(matrix, i, j) == 1):
                arr.append(matrix[i][j])
    if(arr == []):
        print(-1)
    else:
        print(min(arr))


def check(matrix, a, b):
    for direction in directions:
        z = checkEachDirection(matrix, a, b, direction, 0)
        if(z == 1):
            return 1
    return 0


def checkEachDirection(matrix, a, b, direction, c):
    if(c > 2):
        return 1
    x, y = a + direction[0], b + direction[1]
    if(x > -1 and y > -1 and x < m and y < n and matrix[a][b] == matrix[x][y]):
        z = checkEachDirection(matrix, x, y, direction, c + 1)
        if(z == 1):
            return 1
        else:
            return 0
    return 0


m = int(input("m : "))
# n = int(input("n : "))
print("Enter elements in columns : ")
matrix = [[int(j) for j in input().split()] for i in range(m)]
n = len(matrix[0])
consecutivePath(matrix)
