def dele(i, j): # 이어진 연못을 모두 0으로 만드는 작업
    mat[i][j] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for k in range(4):
        x, y = i + dx[k], j + dy[k] #방향 설정
        while 0 <= x < N and 0 <= y < M and mat[x][y]: # 뒷마당의 범위 안에 들어오고 연못이면
            dele(x, y) # 해당 연못을 삭제 후 주변 연못 탐색

T = int(input())
for tc in range(1, T+1):
    result = 0
    M, N, K = map(int, input().split())
    mat = [[0] * M for _ in range(N)] # 뒷마당 생성
    # 연못 생성
    for _ in range(K):
        i, j = map(int, input().split())
        mat[j][i] = 1
    # 뒷마당을 돌면서 연못이면 카운트
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1: # 연못을 발견하면
                dele(i, j) # 이어진 연못을 모두 0으로 만듬
                result += 1 # 이어진 연못을 세는 결과값에 1을 더함
    print(f'#{tc} {result}')