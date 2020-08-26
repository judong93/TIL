def fibo(n):
    if n < 2 : #basis
        return n
    else: #유도파트

        return fibo(n-1) + fibo(n-2)