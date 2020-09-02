def f(n, k): #n열을 선택하는 행번호, k 전체 행과 열의 크기
        global minv
        if n == k: # 모든 행에서 선택이 끝나면
            s = 0
            for i in range(k):
                s += A[i][p[i]] #i행, p[i] i행에서 고른열
            if minv > s:
                minv = s

        else: # 남은 행이 있으면
            for j in range(k):
                if u[j] == 0: # j가 아직 선택하지 않은 열이면
                    u[j] = 1 # j를 표시해서 n+1 이후의 행에서 사용을 막음
                    p[n] = j #n번 행에서 j열을 선택했음을 기록
                    f(n+1, k) # 다음 행에서 열을 선택하러 이동
                    u[j] = 0 # 다른 행에서 사용할 수 있도록 풀어줌

def f(n, k, s): # 열을 선택하는 행번호 n, k 전체 행과 열의 크기, s n-1행까지 선택한 원소값의 합
    global minv
    if n == k: # 모든 행에서 열을 선택하면
        if minv > s:
    elif minv <= s:
        return
    else: # 남은 행이 있으면
        for j in range(k): # 사용하지 않는 열을 찾아서
            if u[j] == 0: # j열을 선택한 적이 없으면
                u[j] = 1 # 선택했음으로 표시
                f1(n+1, k, s+A[n[j]]) # n번행까지 선택한 원소의 합을 구해서 n+1행으로 이동
                u[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    u = [0] * N # 이미 선택한 열을 표시
    p = [0] * N # 선택한 열을 저장 p[n]: n번 행에서 선택한 열 번호
    minv = 10000000
    # f(0, N)
    f1(0, N, 0)