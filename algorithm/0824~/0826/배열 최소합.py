def f(x, summ):
    global minv
    if x == N:
        if summ < minv:
            minv = summ
    elif summ >= minv:
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                f(x+1, summ + mat[x][i])
                v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    minv = 10 * 10
    v= [0] * N
    f(0,0)
    print(f'#{tc} {minv}')