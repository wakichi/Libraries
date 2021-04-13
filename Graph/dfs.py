# グラフGと頂点vを受け取る
def dfs(G, v):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(G, next_v)

if __name__ =="__main__":
    n,m = map(int,input().split())
    Graph = [[] for _ in range(n)]
    seen = [False]*n
    # 有向グラフの場合
    for i in range(m):
        a,b = map(int,input().split())
        Graph[a].append(b)

    for v in range(n):
        if seen[v]: continue
        dfs(Graph, v)

