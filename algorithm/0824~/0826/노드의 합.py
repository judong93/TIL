T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        heap[a] = b
    if 2*(N-M) + 1 > N:
        heap[N-M] = heap[N]
    else:
        heap[N-M] = heap[N] + heap[N-1]
    for i in range(N-M-1,0,-1):
        heap[i] = heap[2*i] + heap[2*i+1]
    result = heap[L]
    print(f'#{tc} {result}')