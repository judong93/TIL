def tor(i, j):
    if i == j:
        return i
    x1 = tor(i, (i+j) // 2)
    x2 = tor(((i+j) // 2)+1, j)
    p1 = card[x1-1]
    p2 = card[x2-1]
    if p2 - p1 == 1 or p2 -p1 == -2:
        return x2
    else:
        return x1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc} {tor(1,N)}')