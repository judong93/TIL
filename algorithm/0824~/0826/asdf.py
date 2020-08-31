def trs(lst, N, M) :
    t_lst = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t_lst[i][j] = lst[j][i]
            return lst

