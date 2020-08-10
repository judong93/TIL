T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = long = number = summ = max_sum = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            if cnt == 0:
                summ += arr[i] + arr[i+1]
                cnt += 1
            else:
                cnt += 1
                summ += arr[i+1]
        if arr[i] >= arr[i+1] or i == len(arr) - 2:
            if long < cnt:
               long = cnt
               max_sum = summ
            if long == cnt and summ > max_sum:
                max_sum = summ
            if cnt >= 1:
                number += 1
            cnt = sum = 0
    print(f'#{tc} {number} {max_sum}')