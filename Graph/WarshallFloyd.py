INF = float('inf')

def warflo(n, m):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    return dp


if __name__ == "__main__":
    n,m = map(int,input().split())
    dp = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] =0
    
    for j in range(m):
        # 1-index
        a,b,w = map(int,input().split())
        dp[a-1][b-1] = w
        dp[b-1][a-1] = w
    from pprint import pprint
    pprint(warflo(n,dp))
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