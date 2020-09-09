def bake(q, N):
    while len(q) > 1:
        x = q.pop(0) # 맨 먼저 넣은 거 꺼내기
        pizzas[x] = pizzas[x] // 2
        if pizzas[x] == 0 and N < M: # 치즈 다 녹았으면
            q.append(N) # 다음번째 피자 넣기
            N += 1
        elif pizzas[x] != 0: # 덜 녹았으면
            q.append(x) # 다시 집어 넣기
    return q.pop(0) + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    q = list(range(N))
    print(f'#{tc} {bake(q, N)}')
