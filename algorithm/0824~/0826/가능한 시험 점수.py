

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    # 깊이 우선일 때 쓸 visit, 높이별로 체크해둔다음 같은 높이에 중복되면 리턴!
    # visit = [[0] * (sum(score) + 1) for _ in range(N+1)] #  마지막에 중복을 제거하기 위해
    visit = [0] * (sum(score) +1)

    # def dfs(k, s):
    #     if visit[k][s]: return
    #     visit[k][s] = 1
    #     if k == N:
    #         return
    #     else:
    #         dfs(k+1, s) # k번 문제를 틀린 경우
    #         dfs(k+1, s+ score[k]) # k번 문제 맞은 경우
    # dfs(0, 0)

    # Q = [[0,0]] # k, s(깊이, 합)
    # while Q:
    #     k, s = Q.pop(0)
    #     if k == N:
    #         visit[s] = 1
    #     else:
    #         Q.append([k+1, s])
    #         Q.append([k+1, s + score[k]])

    Q = [0]
    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] + val]: continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)
    print(f'#{tc} {sum(visit)+1}')