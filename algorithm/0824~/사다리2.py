def ladder(y, x=99):
    cnt = 0
    while x:
        if y-1 >= 0 and mat[x][y-1]:
            while y-1 >=0 and mat[x][y-1]:
                y -= 1
                cnt += 1
        elif y+1 <= 99 and mat[x][y+1]:
            while y+1 <= 99 and mat[x][y+1]:
                y += 1
                cnt += 1
        x -= 1
        cnt += 1
    return y, cnt

for _ in range(10):
    tc = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    minv = 100*100
    result = 0
    for i in range(100):
        if mat[99][i] == 1:
            y, cnt = ladder(i)
            if cnt < minv:
                minv = cnt
                result = y
            elif cnt == minv and y > result:
                result = y
    print(f'#{tc} {result}')