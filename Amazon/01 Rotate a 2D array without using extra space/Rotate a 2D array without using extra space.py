class Solution:
    def rotateMatrix(self, arr, n):
        l = n
        for i in range(l):
            for j in range(i, l):
                a = arr[j][i]
                arr[j][i] = arr[i][j]
                arr[i][j] = a
        for i in range(l//2):
            for j in range(l):
                a = arr[l-i-1][j]
                arr[l-i-1][j] = arr[i][j]
                arr[i][j] = a


if __name__ == '__main__':
    n = int(input())
    inputLine = list(map(int, input().strip().split()))
    arr = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = inputLine[i * n + j]
    ob = Solution()
    ob.rotateMatrix(arr, n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
    print()
