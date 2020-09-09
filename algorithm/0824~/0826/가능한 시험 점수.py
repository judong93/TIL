def dfs(x = 0, s = 0):
    if x == N:
        result.append(s)
        return
    dfs(x+1, s)
    dfs(x+1, s + scores[x])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = []
    dfs()
    print(f'#{tc} {len(set(result))}')