T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    put = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * (N+2) for _ in range(N+2)]
    C = N // 2
    board[C][C+1] = board[C+1][C] = 1
    board[C+1][C+1] = board[C][C] = 2
    drs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    for i in range(M):
        p = put[i] # i번째 두는 동작 리스트로 접근.
        x, y = p[1], p[0]
        board[x][y] = p[2] # 바둑돌 두기.
        for dr in drs:
            j, k, stack = x+dr[0], y+dr[1], []
            while board[j][k]:
                if board[j][k] != p[2]:
                    stack.append((j,k))
                    j, k = j+dr[0], k+dr[1]
                else:
                    for l, m in stack:
                        board[l][m] = p[2]
                    break
    result = [0, 0, 0]
    for a in range(1, N+1):
        for b in range(1, N+1):
            result[board[a][b]] += 1
    print(f'#{tc} {result[1]} {result[2]}')

