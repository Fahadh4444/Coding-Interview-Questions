# User function Template for python3
class Solution:
    def recur(self, l, ob, cb, s):
        if(cb == 0):
            return l.append(s)
        else:
            if(ob >= cb):
                s = s + "("
                self.recur(l, ob-1, cb, s)
            else:
                x = s + "("
                y = s + ")"
                self.recur(l, ob, cb-1, y)
                if(ob > 0):
                    self.recur(l, ob-1, cb, x)

    def AllParenthesis(self, n):
        Result = []
        string = ""
        self.recur(Result, n, n, string)
        return Result


if __name__ == "__main__":
    n = int(input())
    ob = Solution()
    result = ob.AllParenthesis(n)
    result.sort()
    for i in range(0, len(result)):
        print(result[i])
    exit()
