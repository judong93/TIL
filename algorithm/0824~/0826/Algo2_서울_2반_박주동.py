dx = [-1,0,1,0] # 네 방향 설정
dy = [0,1,0,-1]

def exp(R, C): # 폭발 함수
    global cnt
    K = arr[R][C] # 폭발 범위 지정
    arr[R][C] = 0 # 폭발했으므로 폭탄을 없앰
    for i in range(4): # 네 방향으로 돌고
        for j in range(1,K+1): # 폭발 범위만큼 퍼짐
            x = R + (dx[i] * j)
            y = C + (dy[i] * j)
            if 0 <= x < N and 0 <= y < N and arr[x][y] != 0: # 폭발 범위가 지도 안에 있고, 폭탄이 있으면
                cnt += 1 # 폭발 횟수를 추가
                exp(x,y) # 폭발
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1 # 폭발 횟수 카운트, 처음을 미리 셈
    exp(R,C) # 폭발 시작
    print(f'#{tc} {cnt}')
