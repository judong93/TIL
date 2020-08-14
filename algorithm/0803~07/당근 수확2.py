T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    summ = 0
    i = 0
    while i < N-1:
        while arr[i] >= M:
            arr[i] -= M
            summ += (i+1) * 2
        arr[i+1] += arr[i] % M
        i += 1
    if arr[N-1] % M == 0:
        summ += N * (arr[N-1] // M)
    else:
        summ += N * ((arr[N-1] // M) + 1)

    print(f'#{tc} {summ}')