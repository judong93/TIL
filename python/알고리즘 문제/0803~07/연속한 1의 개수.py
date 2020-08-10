T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    maxv = 0
    for i in arr:
        if i == 1:
            cnt += 1
        if i == 0:
            cnt = 0
        if maxv < cnt:
            maxv = cnt
    print(f'#{tc} {maxv}')