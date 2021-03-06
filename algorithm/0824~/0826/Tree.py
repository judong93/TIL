'''
5 4
2 1 2 4 4 3 4 5

'''

def f(n): # n번 노드 방문, 방문후 유효한 노드인지 검사
    if n > 0: # 유효한 노드면
        # print(n) #n번 노드에서 할일(노드에 방문하자마자 처리, 전위순회 preorder)
        f(left[n]) # 왼쪽 자식으로 이동
        # print(n)  # n번 노드에서 할일(왼쪽 자식에서 리턴 후, 중위순회, inorder)
        f(right[n]) # 오른쪽 자식으로 이동
        print(n)  # n번 노드에서 할일(왼쪽 자식에서 리턴 후, 후위순회, postorder)

def f2(n):
    print(n)
    if left[n] > 0:
        f2(left[n])
    if right[n] > 0:
        f2(right[n])


# 1번부터 V번까지 노드, E개의 간선
V, E = map(int, input().split())
edge = list(map(int, input().split()))
left = [0] * (V+1) # 부모를 인덱스로 왼쪽 자식번호 저장
right = [0] * (V+1) # 부모를 인덱스로 오른쪽 자식번호 저장
pa = [0] * (V+1)
root = 0
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1] # n1 = 부모, n2 자식노드
    if left[n1] == 0: # 왼쪽 자식이 없으면
        left[n1] = n2 # 부모를 인덱스로 자식번호 저장
    else: # 왼쪽 자식이 있으면
        right[n1] = n2  # 부모를 인덱스로 자식번호 저장

    pa[n2] = n1 # 자식을 인덱스로 부모를 저장
for i in range(1, V+1):
    if pa[i] == 0: # 부모가 없으면 root
        root = i
        break
f(root) # 주어진 입력의 root부터 순회
