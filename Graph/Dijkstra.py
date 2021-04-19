from BaseGraph import WeightGraph

INF = float('inf')
def dijkstra(graph,n,start):
    # define variables
    used = [False]*n
    dist = [INF]*n
    #　初期化
    dist[start] = 0
    for i in range(n):
        # usedではない変数のうち、最小のものを探す
        min_dist = INF
        min_v = -1
        # 全頂点を探索
        for v in range(n):
            if not used[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v
        print(min_v)
        # 存在しないならば、終了
        if min_v == -1:
            break

        # min_vをスタートとして、各辺を緩和
        for e in graph.output(min_v):
            dist[e[0]] = min(dist[e[0]], dist[min_v] + e[1])

        used[min_v] = True
    return dist


if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = WeightGraph(n,m)
    graph._input()
    start_node = 0
    dis = dijkstra(graph,n,start_node)
    print(dis)

"""
10 11
1 2 10
1 3 20
1 4 30
1 6 40 
3 7 50 
1 8 60 
1 9 70 
4 10 80 
10 2 70 
3 5 60 
6 8 50
"""