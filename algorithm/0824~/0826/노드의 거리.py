def bfs(s, e):
    q = [s]
    v[s] = 1
    while q:
        x = q.pop(0)
        for i in range(V+1):
            if mat[x][i] == 1 and v[i] == 0:
                q.append(i)
                v[i] = v[x] + 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    mat = [[0] * (V+1) for _ in range(V+1)]
    v = [0] * (V+1)
    for i in range(E):
        a, b = map(int,input().split())
        mat[a][b] = 1
        mat[b][a] = 1
    s, e = map(int, input().split())
    bfs(s, e)
    result = v[e] - 1
    if v[e] == 0:
        result = 0
    print(f'#{tc} {result}')
