def subset(k=0, s=0):
    global ans
    if k == N:
        if s >= B and s < ans:
            ans = s
        return
    if s > ans:
        return
    subset(k+1, s)
    subset(k+1, s + H[k])



T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = sum(H)
    subset()
    print(f'#{tc} {ans-B}')
