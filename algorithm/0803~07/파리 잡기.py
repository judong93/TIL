T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    for i in range(N):
        for j in range(N):
            summ = 0
            for k in range(M):
                for l in range(M):
                    if i+k < N and j+l < N:
                        summ += arr[i+k][j+l]
            if maxv < summ:
                maxv = summ
    print(f'#{tc} {maxv}')