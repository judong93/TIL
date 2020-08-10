T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    minv = arr[0]
    minI = 1
    for i in range(len(arr)):
        if minv > arr[i]:
            minv = arr[i]
            minI = i+1
    print(f'#{tc} {minI}')