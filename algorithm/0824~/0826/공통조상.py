def search(v1): # 공통 조상 찾기
    global q
    pa_v1 = tree[v1][2] # v1의 부모
    if pa_v1: # 부모가 존재하면
        if pa_v1 not in q: # 부모가 q에 없으면 담음
            q.append(pa_v1)
        else: # 부모가 존재하면 공통된다는 뜻이므로 스톱하고 리턴
            return pa_v1
        return search(pa_v1)
    else: # 부모가 존재하지 않으므로 루트임. 따라서 공통조상은 루트뿐
        return 0

def subtree(v): # 서브트리 노드 수 체크
    global cnt
    if v:
        subtree(tree[v][0])
        cnt += 1
        subtree(tree[v][1])


T = int(input())
for tc in range(1, T+1):
    V, E, V1, V2 = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    q = []
    cnt = 0
    for i in range(E): # tree[i][0]이 left, [1]이 right. [2]이 부모
        a, b = temp[2*i], temp[(2*i)+1]
        if tree[a][0] == 0:
            tree[a][0] = b
        else:
            tree[a][1] = b
        tree[b][2] = a
    v = search(V1) + search(V2) # 공통 부모 찾기
    subtree(v)
    print(f'#{tc} {v} {cnt}')