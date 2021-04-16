from BaseGraph import WeightGraph
INF = 10**11
def belfor(graph,n,m,start):
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
    exist_negative_cycle = False
    start_node = 2
    dis = belfor(graph,n,m,start_node)
    if dis == []:
        print("exist negative cycle")
    else:
        for i in range(n):
            print(i, dis[i] if dis[i]!= INF else "INF")

    