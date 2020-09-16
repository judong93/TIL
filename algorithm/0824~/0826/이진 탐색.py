def inorder(s):
    global cnt
    if s <= N:
        inorder(s*2)
        number[s] = cnt
        cnt += 1
        inorder(s*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = [0] * (N+1)
    cnt = 1
    inorder(1)

    print(f'#{tc} {number[1]} {number[N//2]}')