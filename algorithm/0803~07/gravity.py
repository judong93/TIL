T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxv = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                cnt += 1
        if cnt > maxv:
            maxv = cnt
    print(f'#{tc} {maxv}')