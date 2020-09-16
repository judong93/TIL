arr = [1,2,3,4]
N = len(arr)

# binary counting을 통한 부분집합 생성
# for bit in range(1 << N): # N이 최대 16이므로,. 최대 2의 16승. 이정도는 해도 됨.
#     A, B = [], []
#     for i in range(N):
#         if bit & (1 << i): A.append(arr[i])
#         else: B.append(arr[i])
#     if len(A) == len(B):
#         print(A,B)

def subset(k): # k: 함수 호출의 깊이
    if k == N:
        if len(A) == len(B):
            print(A, B)
    else:
        A.append(arr[k])
        subset(k+1) # k번 요소를 A에 포함하는 선택
        A.pop()

        B.append(arr[k])
        subset(k+1) # k번 요소를 B에 포함하는 선택
        B.pop()

A, B = [arr[0]], []
subset(1)