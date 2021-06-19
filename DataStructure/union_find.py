class UnionFind:
    """
    頂点はそれぞれ0~n-1の値を入れる
    # tips: 上記を満たさない場合、辞書を使うとうまくいく
    parは各頂点の親を表す。rootの場合は-1
    sizは拡張点の属する木の頂点数
    nは大きさ
    """

    def __init__(self, n):
        """
        n:含むであろう木の大きさ
        初期化メソッド
        """
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int):
        """
        x:int(頂点の番号)
        xの一番親を求める。
        返り値はその親の頂点番号
        """
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def is_same(self, x: int, y: int):
        return (self.root(x) == self.root(y))

    def unite(self, x, y):
        """
        x, y:int(頂点の番号)
        xとyを同じ木とする。
        """
        # xとyをそれぞれrootまで移動する。
        x = self.root(x)
        y = self.root(y)
        # すでに同じグループの時
        if(x == y):
            return False
        # union by size
        if (self.siz[x] < self.siz[y]):
            (x, y) = (y, x)
        # yの方がサイズが小さい
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        """
        x:int(頂点の番号)
        xを含む木に含まれる頂点数を求める
        """
        return self.siz[self.root(x)]

    def connected(self):
        """
        連結成分の個数を返す（未検証）
        """
        st = set()
        for i in range(self.n):
            st.add(self.root(i))
        return len(st)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    for i in range(m):
        a, b = map(int, input.split())
        # a,b が 1-startの場合
        uf.unite(a - 1, b - 1)
    print(uf.is_same(1, 3))
    print(uf.is_same(2, 5))
