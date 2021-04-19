# n は制約の数、mは非規定変数の数
n,m = map(int, input().split())

lis = [[1] for _ in range(m)]*(n+1)
for i in range(n):
    lis[1:] = list(map(int, input().split()))

class Symplex:
    ans = [0]*10
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.lis = [[None] for _ in range(m)]*(n+1)
    
    def _input(self):
        for i in range(n):
            self.lis[i] = list(map(int, input().split()))

    def find_c(self):
        self.m = 0
        for i in range(m):
            if lis[-1][i]<0:
                self.m = lis[-1][i]
                break
        else:
            return self.ans
    
    def find_r(self):
        self.inx_temp = 0
        self.min_temp = 10**10
        for i in range(n):
            if self.lis[][i] !=0 and self.lis[][]/self.lis[][] <self.min_temp:
                self.inx_temp = i
                self.min_temp = self.lis[][]/self.lis[][]

    def pivot(self):
        
    def solve(self):



if __name__ == "__main__":
    n,m = map(int, input().split())

    sym = Symplex(n,m)
    sym._input()

