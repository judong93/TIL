T =int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    minv =  10 ** 10
    last_area = 0
    for i in range(len(arr)):
        sum1 = 0
        sum2 = 0
        for j in range(i+1):
            sum1 += arr[j]
        for k in range(len(arr)-1, i, -1):
            sum2 += arr[k]
        if abs(sum1 - sum2) < minv:
            minv = abs(sum1 - sum2)
            last_area = i + 1
    print(f'#{tc} {last_area} {minv}')