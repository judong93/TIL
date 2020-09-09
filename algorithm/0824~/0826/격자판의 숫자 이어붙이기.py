dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move(i, j, summ): # 6번 움직이기
    a = summ + mat[i][j]
    if len(a) == 7:
        sums.append(a)
        return
    for l in range(4):
        x, y = i + dx[l], j + dy[l]
        if 0 <= x < 4 and 0 <= y < 4:
            move(x, y, a)

T = int(input())
for tc in range(1, T+1):
    mat = [list(input().split()) for _ in range(4)]
    sums = []
    for i in range(4):
        for j in range(4):
            move(i, j, '')
    print(f'#{tc} {len(set(sums))}')