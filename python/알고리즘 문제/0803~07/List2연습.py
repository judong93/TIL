T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    sumv = 0
    for i in range(N):
        for j in range(N):
            for k in range(len(dj)):
                testI = i + di[k]
                testJ = j + dj[k]
                if 0<= testI < N and 0 <= testJ < N:
                    sumv += abs(arr[i][j] - arr[testI][testJ])
    print(f'#{tc} {sumv}')