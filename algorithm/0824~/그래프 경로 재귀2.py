def dfs(s):
    visited[s] = 1
    for i in range(V+1):
        if adj[s][i] == 1 and visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        tmp = list(map(int, input().split()))
        n1 = tmp[0]
        n2 = tmp[1]
        adj[n1][n2] = 1
    s, e = map(int, input().split())
    dfs(s)
    result = 0
    if visited[e]:
        result = 1
    print(f'#{tc} {result}')