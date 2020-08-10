T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chem = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1
                chem.append([r - i, c - j])
                for p in range(i, r):
                    for q in range(j, c):
                        arr[p][q] = 0
            chem.sort(key=lambda x: x[0])
            chem.sort(key=lambda x: x[0] * x[1])
            print(f'#{tc} {len(chem)}', end=' ')
            for x in chem:
                print(*x, end=' ')
            print()
