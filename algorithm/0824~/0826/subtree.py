def search(s):
    global cnt
    if s == 0:
        return
    if s:
        search(left[s])
        cnt += 1
        search(right[s])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    temp = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)
    cnt = 0
    for i in range(E):
        if left[temp[2 * i]] == 0:
            left[temp[2 * i]] = temp[(2 * i) + 1]
        else:
            right[temp[2 * i]] = temp[(2 * i) + 1]
    search(N)
    print(f'#{tc} {cnt}')