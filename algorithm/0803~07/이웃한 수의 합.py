T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = arr[i]
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] > max_sum:
            max_sum = arr[i] +arr[i+1]
        if arr[i] + arr[i+1] < min_sum:
            min_sum = arr[i] +arr[i+1]
    print(f'#{tc} {max_sum} {min_sum}')