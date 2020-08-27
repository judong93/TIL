def dfs(s, e):
    visited = [0] * (V+1)
    stack = [s]
    visited[s] = 1

    while stack:
        n = stack.pop()
        if n == e:
            return 1
        for i in range(V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        tmp = list(map(int, input().split()))
        n1 = tmp[0]
        n2 = tmp[1]
        adj[n1][n2] = 1
    s, e = map(int, input().split())
    result = dfs(s, e)
    print(f'#{tc} {result}')

