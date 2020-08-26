def dfs(s, e):
    visited = [0]* (e+1)
    stack = [s]
    visited[s] = 1

    while stack:
        n = stack.pop()
        if n == 99:
            return 1
        for i in range(e+1):
            if adj[n][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    adj = [[0]*100 for _ in range(100)]
    tmp = list(map(int, input().split()))
    for i in range(E):
        n1 = tmp[i*2]
        n2 = tmp[(i*2)+1]
        adj[n1][n2] = 1
    result = dfs(0, 99)
    print(f'#{tc} {result}')
