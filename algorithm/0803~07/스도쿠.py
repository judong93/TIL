def f3():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 10
            for k in range(3):
                for l in range(3):
                    if cnt[sudoku[i + k][j + l]] == 0:
                        cnt[sudoku[i + k][j + l]] = 1
                    else:
                        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        cnt = [0] * 10 # index 1에서 9에 대해 카운트 배열
        for j in range(9):
            if cnt[sudoku[i][j]] == 0:
                cnt[sudoku[i][j]] = 1
            else: # 겹치는 숫자가 있으면
                ans = 0
                break # for j를 빠져나감.
        if ans == 0:
            break # for i를 빠져나감.
    if ans:
        for j in range(9):
            cnt = [0] * 10
            for i in range(9):
                if cnt[sudoku[i][j]] == 0:
                    cnt[sudoku[i][j]] = 1
                else:
                    ans = 0
                    break
            if ans == 0:
                break

    if ans:
        ans = f3()

    print(f'#{tc} {ans}')
