T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum1 = sum2 = sum3 = sum4 = 0

    for i in range(N):
        for j in range(N):
            if i < j and i+j < N-1:
                sum1 += arr[i][j]
            elif i < j and i+j > N-1:
                sum2 += arr[i][j]
            elif i > j and i+j > N-1:
                sum3 += arr[i][j]
            elif i > j and i+j < N-1:
                sum4 += arr[i][j]
    sum_list = [sum1, sum2, sum3, sum4]
    result = max(sum_list) - min(sum_list)
    print(f'#{tc} {result}')