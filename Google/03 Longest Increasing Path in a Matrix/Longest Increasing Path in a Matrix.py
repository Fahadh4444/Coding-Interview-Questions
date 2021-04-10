directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    maxLength = 0
    cache = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            eachLength = checking(matrix, cache, n, m, i, j)
            maxLength = max(eachLength, maxLength)
    return maxLength


def checking(matrix, cache, n, m, a, b):
    if(cache[a][b] > 0):
        return cache[a][b]
    maxL = 0
    for direction in directions:
        x, y = a + direction[0], b + direction[1]
        if(x > -1 and y > -1 and x < m and y < n):
            if(matrix[x][y] > matrix[a][b]):
                length = checking(matrix, cache, n, m, x, y)
                maxL = max(maxL, length)
    cache[a][b] = maxL + 1
    return cache[a][b]


m = int(input("m : "))
n = int(input("n : "))
print("Enter elements in columns : ")
matrix = [[int(j) for j in input().split()] for i in range(m)]
print(matrix)
print(longestIncreasingPath(matrix))
