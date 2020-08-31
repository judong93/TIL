T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if mat[i][j] == 0:
                if cnt == 3:
                    result += 1
                cnt = 0

            elif mat[i][j] == 1:
                cnt += 1
                if j == N-1 and cnt == 3:
                    result += 1
        cnt = 0
        for k in range(N):
            if mat[k][i] == 0:
                if cnt == 3:
                    result += 1
                cnt = 0

            elif mat[k][i] == 1:
                cnt += 1
                if k == N-1 and cnt == 3:
                    result += 1
    print(f'#{tc} {result}')