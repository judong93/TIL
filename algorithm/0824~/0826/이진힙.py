def add(i):
    global last
    last += 1
    heap[last] = i
    a = last
    while a // 2:
        if heap[a] < heap[a // 2]:
            heap[a], heap[a // 2] = heap[a // 2], heap[a]
            a = a // 2
        else:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0
    for i in arr:
        add(i)
    x = N // 2
    summ = 0
    while x:
        summ += heap[x]
        x //= 2
    print(f'#{tc} {summ}')