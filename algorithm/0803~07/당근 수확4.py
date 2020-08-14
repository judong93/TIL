T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    c = (N-1) // 2 # 각 행과 열의 중간값
    di = [0, c, c, N-1] # 네 부분의 중심이 되는 점을 지정하기 위함.
    dj = [c, 0, N-1, c] # ''
    move1 = [] # 각 구간의 중심점에서 주변으로 움직일 값, 각각 상하좌우로 움직일 것임.
    move2 = []  # ''
    result = []
    for j in range(1, (N // 2)): #move에 밸류를 넣는 작업 , N//2-1은 상하좌우로 각 몇번씩 갈것인지를 나타냄.
        move1.extend([j, -j])
        move2.extend([j, -j])

    for i in range(4):  # 네개의 구간별 중심점으로 가는 작업
        summ = arr[di[i]][dj[i]] # 구간별 합계의 초기값을 구간의 중간점으로 지정.
        for k in range(((N // 2) - 1) * 2):
            testi = di[i] + move1[k]
            testj = dj[i] + move2[k]
            if 0 <= testi < N:
                summ += arr[testi][dj[i]] # 중간값에서 상하로만 이동해서 결과값 더함
            if 0 <= testj < N:
                summ += arr[di[i]][testj] # 중간값에서 좌우로만 이동해서 결과값 더함
        result.append(summ)
    diff = max(result) - min(result)
    print(f'#{tc} {diff}')

    # 로직 자체를 잘못 짰으나, 이것도 어쩄든 짜느라 고생했으므로 저장.