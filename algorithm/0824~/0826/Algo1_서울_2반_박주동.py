T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sums = [] # 각 테두리의 합을 담을 리스트 생성
    for i in range(N-K+1): # 테두리를 생성할 수 있는 범위를 설정
        for j in range(M-K+1): # 테두리를 생성할 수 있는 범위를 설정
            summ = 0 # 테두리의 합을 담을 변수 생성
            for k in range(K): # 테두리 안에 있는 모든 수를 더하는 과정
                for l in range(K):
                    summ += arr[i+k][j+l]
            for m in range(K-2): # 테두리 안쪽에 있는 수를 빼는 과정
                for n in range(K-2):
                    summ -= arr[i+1+m][j+1+n]
            sums.append(summ) # 테두리 값을 더한 결과를 리스트에 추가
    print(f'#{tc} {max(sums) - min(sums)}')
