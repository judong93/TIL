T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    result = n * m

    white = 0
    for i in range(n - 2):
        for j in range(0, m):
            if flag[i][j] != 'W':
                white += 1

        blue = 0
        for k in range(i + 1, n - 1):
            for l in range(0, m):
                if flag[k][l] != 'B':
                    blue += 1

            red = 0
            for r in range(k + 1, n):
                for s in range(0, m):
                    if flag[r][s] != 'R':
                        red += 1

            total = white + blue + red
            if result > total:
                result = total

    print(f'#{tc} {result}')