def bfs(s, M):
    q.append(s)
    v[s] = 1

    while q:
        s = q.pop(0)
        for i in range(M+1):
            if G[s][i] == 1 and v[i] == 0:
                q.append(i)
                v[i] = v[s] + 1

for tc in range(1, 11):
    X, s = map(int, input().split()) # M = 2 * Edge
    N = X // 2
    temp = list(map(int, input().split()))
    M = max(temp)
    G = [[0] * (M+1) for _ in range(M+1)]
    for i in range(N):
        G[temp[2*i]][temp[2*i+1]] = 1
    v = [0] * (M+1)
    q = []
    maxI = 0
    bfs(s, M)

    for j in range(M+1):
        if v[j] >= v[maxI]:
            maxI = j
    print(f'#{tc} {maxI}')