for tc in range(1, 11):
    N = int(input())
    tree = [[]]
    for i in range(1,N +1):
        tree.append(list(input().split()))
        if len(tree[i]) == 4:
            tree[i][2] = int(tree[i][2])
            tree[i][3] = int(tree[i][3])
        else:
            tree[i][1] = int(tree[i][1])

    def calc(v):
        if len(tree[v]) == 2:
            return tree[v][1]
        else:
            l = calc(tree[v][2])
            r = calc(tree[v][3])

            if tree[v][1] == '+': return 1 + r
            elif tree[v][1] == '-': return 1-r
            elif tree[v][1] == '*': return 1*r
            else: return l / r
    calc(1)

