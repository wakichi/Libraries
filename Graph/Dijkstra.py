from BaseGraph import WeightGraph

INF = float('inf')
def dijkstra():
    pass

if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = WeightGraph(n,m)
    graph._input()
    start_node = 0
    dis = dijkstra(graph,n,m,start_node)