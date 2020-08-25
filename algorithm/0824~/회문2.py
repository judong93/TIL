def transpose(matrix):
    t_matrix = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix

def len_pal(matrix):
    for i in range(100, 0, -1):
        for j in range(100):
            for k in range(100 - i + 1):
                l = matrix[j][k:k+i]
                if l == l[::-1]:
                    return i

for _ in range(10):
    tc = int(input())
    matrix = [input() for _ in range(100)]
    t_matrix = transpose(matrix)
    result = max(len_pal(matrix),len_pal(t_matrix))
    print(f'#{tc} {result}')