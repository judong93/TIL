def inorder(n=1):
    if n:
        inorder(left[n])
        print(word[n], end='')
        inorder(right[n])

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    word = [0]
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in arr:
        word.append(i[1])
    for i in arr:
        if len(i) > 2:
            for j in range(2, len(i)):
                if left[int(i[0])] == 0:
                    left[int(i[0])] = int(i[j])
                else:
                    right[int(i[0])] = int(i[j])
    print(f'#{tc}', end= ' ')
    inorder()
    print()
