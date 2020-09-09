def R(x):
    v[x] = 1
    for i in range(N+1):
        if r[x][i] == 1 and v[i] == 0:
            R(i)

def check(i):
    global cnt
    cnt += 1
    R(i)
    for j in range(N+1):
        if v[j] == 0:
            check(j)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    r = [[0] * (N+1) for _ in range(N+1)]
    temp = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        a, b = temp[i][0], temp[i][1]
        r[a][b] = 1
        r[b][a] = 1
    v = [0] * (N+1)
    v[0] = 2
    cnt = 0
    check(1)
    print(f'#{tc} {cnt}')