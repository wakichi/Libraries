class UnionFind:
    #parは各頂点の親を表す。rootの場合は-1
    #sizは拡張点の属する木の頂点数
    # nは大きさ
    def __init__(self, n):
        self.par = [-1]*n
        self.siz = [1]*n
    
    
    def root(self,x:int):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    

    def is_same(self,x:int, y:int):
        return (self.root(x) == self.root(y))
    

    def unite(self,x, y):
        # xとyをそれぞれ\rootまで移動する。
        x = self.root(x)
        y = self.root(y)
        # すでに同じグループの時
        if(x == y):
            return False
        # union by size
        if (self.siz[x]< self.siz[y]):
            (x,y) = (y,x)
        #yの方がサイズが小さい
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    
    def size(self,x):
        return self.siz[self.root(x)]
        

if __name__ == "__main__":
    n,m,k = map(int, input().split())
    uf = UnionFind(n)
    for i in range(m):
        a,b = map(int,input.split())
        # a,b が 1-startの場合
        uf.unite(a-1,b-1)
    print(uf.is_same(1,3))
    print(uf.is_same(2,5))