# q= [0] * 10
# front = -1
# rear = -1
#
# rear += 1
# q[rear] = 1 # enq(1)
#
# while front != rear:
#     front += 1
#     n = q[front]

def bfs(s, N): # 1~N번 노드가 존재하는 그래프 탐색
    q = [s] #큐생성, 시작점 enq
    v = [0] * (N+1)
    v[s] = 1 # 시작노드 방문표시
    while q:
        t = q.pop(0) #deq
        # 여기서 t노드에 대한 처리

        for i in range(1, N+1): # 인접이고 enq되지 않은 노드
            if adj[t][i] == 1 and v[i] == 0: # adj 인접행렬
                q.append(i) #enq
                v[i] = v[t] + 1# 방문표시
