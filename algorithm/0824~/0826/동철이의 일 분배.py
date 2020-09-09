def choose(i,x): # 행 인덱스, 곱해나갈 변수
    global result
    if i == N:
        if result <= x:
            result = x
        return
    else:
        if x <= result: return
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                choose(i+1, x * chance[i][j] / 100)
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chance = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    result = 0
    choose(0, 1)
    print(f'#{tc} {result * 100: .6f}')
