T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cre = 1
    maxv = 1
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            cre += 1
        else:
            cre = 1
        if maxv < cre:
            maxv = cre
    print(f'{tc} {maxv}')