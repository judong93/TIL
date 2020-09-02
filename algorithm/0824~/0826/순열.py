def perm(n, k): #원하는 뎁스, 현재 뎁스
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1,2,3]
N = len(arr)
perm(N, 0)