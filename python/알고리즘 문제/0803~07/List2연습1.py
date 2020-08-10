T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    result = 0
    for i in range(1, 1 << N):
        S = 0
        for j in range(N):
            if i & (1 << j):
                S += arr[j]
        if S == 0:
            result = 1
            break
    print(f'#{tc} {result}')