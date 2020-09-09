dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(i, j):
    q = [(i,j)]
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < N and 0 <= y < N and maze[x][y] != 1 and v[x][y] == 0:
                q.append((x,y))
                v[x][y] = v[i][j] + 1

def dfs(i, j, N, c): # 가능한 모든 경로를 탐색.. i,j칸에 오기까지 거쳐온 edge 개수 c
    global minv
    if v[i][j] == '3':
        if minv > c:
            minv = c
    elif minv <= c: # 백트래킹
        return
    else:
        v[i][j] = 1 # i,j 이후에 중복 방문 방지
        # i,j에 대해 네 방향 탐색
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < N and 0 <= y < N and maze[x][y] != 1 and v[x][y] == 0:
                dfs(x, y, N, c+1)
        v[i][j] = 0 # i, j 이전에 다른 경로로부터 재 진입 허용용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    starti = 0
    startj = 0
    endi = endj = 0
    v = [[0] * N for _ in range(N)]
    minv = N*N
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                starti = i
                startj = j
            if maze[i][j] == 3:
                endi, endj = i, j
    f(starti, startj)
    result = v[endi][endj] - 2
    if v[endi][endj] == 0:
        result = 0
    print(f'#{tc} {result}')