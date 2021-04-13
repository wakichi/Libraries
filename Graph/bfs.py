from collections import deque

n = 0
m = 0


# input:Graph G and start vertex s
def bfs(G, s) -> list:
    # initialize
    que  = deque()
    dist = [-1]*n
    dist[s] = 0
    que.append(s)

    while len(que) != 0:
        v = que.popleft()

        for x in G[v]:
            if dist[x] != -1: continue

            dist[x] = dist[v] +1
            que.append(x)
    
    return dist

if __name__ =="__main__":
    n,m = map(int,input().split())
    Graph = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        # 1-start
        a-=1
        b-=1
        Graph[a].append(b)
        Graph[b].append(a)
    
    dist = bfs(Graph, 0)
    print(dist)

