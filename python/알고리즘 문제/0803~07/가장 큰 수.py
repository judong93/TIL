T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxv = arr[0]
    for i in arr:
        if i > maxv:
            maxv = i
    print(f'{tc} {maxv}')