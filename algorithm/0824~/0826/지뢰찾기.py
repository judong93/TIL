dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def search(i, j):
    for k in range(8):
        x, y = i +dx[k], j + dy[k] # 8방향을 돌면서
        if 0 <= x < N and 0 <= y < N and area[x][y] == '*': # 지뢰를 발견하면
            area[i][j] = '1' # 원점만 방문처리하고
            return # 끝냄
    for l in range(8): # 지뢰가 없었기 때문에
        x1, y1 = i + dx[l], j + dy[l]
        if 0 <= x1 < N and 0 <= y1 < N:
            area[x1][y1] = '1' # 돌면서 방문표시를 해주고 들어가서 탐색
            search(x1, y1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == '.': # 검사해보지 않았거나 지뢰가 아니라면
                cnt += 1
                search(i, j) # 탐색
    print(f'#{tc} {cnt}')