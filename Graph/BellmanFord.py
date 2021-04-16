from BaseGraph import WeightGraph
INF = float('inf')
def belfor(graph,n,start):
    dist = [INF]*n
    dist[start] = 0
    negative_cycle = False
    for i in range(n):
        update = False
        for v in range(n):
            # dist[v] == INFなら緩和しない
            if dist[v] == INF: continue
            for e in graph.output(v):
                if dist[e[0]]  > dist[v] +e[1]:
                    dist[e[0]] = dist[v] +e[1]
                    update = True
        if not update: break

        if (i == n-1 and update):negative_cycle = True
    if negative_cycle:
        return []
    else:
        return dist


if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = WeightGraph(n,m)
    graph._input()
    start_node = 0
    dis = belfor(graph,n,start_node)
    if dis == []:
        print("exist negative cycle")
    else:
        for i in range(n):
            print(i, dis[i] if dis[i]!= INF else "INF")

"""
sample
6 5 
0 1 3
1 2 -10
2 3 2
3 1 4
1 4 9
"""