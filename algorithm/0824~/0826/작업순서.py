for tc in range(1, 11):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    mat = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        mat[temp[2*i]][temp[(2*i)+1]] = 1
    for j in range(V):
        for k in range(V)