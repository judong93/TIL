T = int(input())
for tc in range(1, T+1):
    N, M, D = map(int, input().split())
    mat = [[0] * N for _ in range(N)] # 빈 행렬 생성
    C = N // 2
    result = []
    mat[C][C] = M # 행렬 정 가운데에 M 값을 할당.
    for i in range(1, 1 + C): # 가운데에서 점차 하나씩 바깥행렬로 이동
        for j in range(C-i, C+i+1): # i만큼 위아래로 커진 행
            for k in range(C-i, C+i+1): # i만큼 양옆으로 커진 열
                if mat[j][k] == 0:
                    mat[j][k] = M + (D * i) # 빈 곳에다 이동수 * 변화값을 더하여 입력
    for l in range(N):
        summ = 0 # 행별로 합을 구한 후 초기화
        for m in range(N):
            summ += mat[l][m] # 행을 돌면서 모두 더함.
        result.append(summ) # 행의 값을 순서대로 결과 리스트에 추가.
    print(f'#{tc}', end=' ')
    for n in range(N):
        print(result[n], end = ' ') # 결과 리스트를 돌면서 출력
    print()