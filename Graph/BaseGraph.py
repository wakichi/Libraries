# 辺の入力は1-スタートとする。

class BaseGraph:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.Graph = [[] for _ in range(self.n)]
    # 初期状態は無効グラフ
    def _input(self,dir_flag=True):
        for _ in range(self.m):
            a,b = map(int,input().split())
            self.Graph[a-1].append(b-1)
            if dir_flag: self.Graph[b-1].append(a-1)

    # 可視化
    def _print(self):
        for lis in self.Graph:
            print(lis)

# グリッドグラフ
# 通れる部分を . 、通れない部分を # とする。
class GridGraph(BaseGraph):
    def __init__(self, n, m, exist="#", not_exist=".", move_eight=False):
        self.n = n
        self.m = m
        self.exist = exist
        self.not_exist = not_exist
        self.Graph = [[None]*n]
        self.move_list = [[1,0,-1,0],[0,1,0,-1]]
        # 動ける場所が４か８か指定
        if move_eight:
            self.move_list[0]+=([-1,1,1,-1])
            self.move_list[1]+=([1,1,-1,-1])
    def _input(self):
        for i in range(self.n):
            grid = input()
            self.Graph[i] = list(map(lambda c: 1 if c == self.exist else 0 , grid))

# グラフのiばんめは、(to, weight)　で格納
class WeightGraph(BaseGraph):
    def __init__(self, n, m):
        super().__init__(n,m)
    # 0-indexに注意
    def _input(self):
        for _ in range(self.m):
            a,b,w = map(int, input().split())
            self.Graph[a].append([b, w])

    def output(self,v):
        return self.Graph[v]


if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = WeightGraph(n,m)
    graph._input()
    graph._print()
    print(graph.output(0))