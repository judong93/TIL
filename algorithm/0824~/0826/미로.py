def f(i, j , N):
    if maze[i][j] == 3:
        return 1
    v[i][j] = 1
    # 인접하고 방문하지 않은 칸이면
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for l in range(4):
        x, y = i + dx[l], j + dy[l]
        if 0 <= x < N and 0 <= y < N and maze[x][y] != 1 and v[x][y] == 0:
            if f(x, y, N):
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    starti = 0
    startj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                starti, startj = i, j
    result = f(starti, startj, N)
    print(f'#{tc} {result}')

