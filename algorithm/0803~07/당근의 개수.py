T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxi = 0
    maxv = arr[0]
    for i in range(len(arr)):
        if maxv < arr[i]:
            maxv = arr[i]
            maxi = i
    print(f'#{tc} {maxi+1} {maxv}')
