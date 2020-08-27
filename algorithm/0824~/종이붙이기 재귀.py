def tiling(w):
    if w == 1:
        return 1
    elif w == 2:
        return 3
    else:
        return tiling(w-1) + (2 * tiling(w-2))

T = int(input())
for tc in range(1, T+1):
    w = int(input()) // 10
    result = tiling(w)
    print(f'#{tc} {result}')

