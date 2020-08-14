T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        if i % 2 == 0:
            cnt += 1
    print(f'#{tc} {cnt}')