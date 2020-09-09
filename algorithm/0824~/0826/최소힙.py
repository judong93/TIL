def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    # 루트가 아니고, 만약에 부모노드 값 > 자식노드값 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent] , heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

def heappop():
    global heapcount
    retValue = heap[1] # root
    heap[1] = heap[heapcount]
    heap[heapcount] = 0 # 맽끝 번호를 루트로 올림! 그러기 위해 힙에서 삭제
    heapcount -= 1

    parent = 1
    child = parent * 2

    if child +1 <= heapcount: #오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1
    # 자식노드가 존재하고, 부모노드 > 자식노드 => swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1
                
#최소힙
heapcount = 0
temp = [7,2,5,3,4,6]
N = len(temp)
heap = [0] * (len(temp)+1)
for i in range(N):
    heappush(temp[i])

for i in range(N):
    print(heappop(), end=' ')
print()