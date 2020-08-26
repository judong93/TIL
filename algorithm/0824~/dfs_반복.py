'''
input 값.
7 8
1 2 1 3 2 4 2 5 3 5 4 6 5 6 6 7

'''
def dfs(s, V): #반복구조의 깊이우선탐색
    #초기화, 스택생성, visited[] 생성 및 초기화
    #stack = [s] # 스택생성, 시작노드 push
    visited = [0]*(V+1) # v[] 생성
    stack = []
    stack.append(s) #push()
    visited[s] = 1

    while stack: # 스택이 비어있지 않으면 반복
        n = stack.pop() # 탐색할 노드 선택 pop()
        #print(n) # n번 노드에서 할일 -> 방문순서대로 출력
        if n == 7: # 7번에 도착하면 1, 못하면 0을 출력
            return 1
        for i in range(1, V+1): # n에 인접하고 방문하지 않은 노드 찾기
            if adj[n][i] == 1 and visited[i] == 0: # i가 n에 인접하고, 미방문이면
                stack.append(i)
                visited[i] = 1
    return 0 # 7번에 도착 못했으므로 0 출력.

V, E = map(int, input().split()) # V 정점 개수, E 간선 개수
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
tmp = list(map(int, input().split())) # E개의 간선 정보
for i in range(E): #인접행렬 기록
    n1 = tmp[i*2]
    n2 = tmp[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우

dfs(1, V) # V개 짜린데 1번부터 탐색하겠다(몇번부터 시작할지는 문제에 나옴)