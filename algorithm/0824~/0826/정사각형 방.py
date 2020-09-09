dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check(i,j,cnt, s):
    global maxv, start
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < N and 0 <= y < N and room[x][y] == room[i][j] + 1:
            cnt += 1
            check(x,y, cnt, s)
            return
    if cnt > maxv:
        maxv = cnt
        start = s
    elif cnt == maxv and s < start:
        start = s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    maxv = 1
    start = (N * N) + 1
    for i in range(N):
        for j in range(N):
            if room[i][j] < start or room[i][j] > start + maxv - 1 :
                check(i,j,1, room[i][j])
    print(f'#{tc} {start} {maxv}')