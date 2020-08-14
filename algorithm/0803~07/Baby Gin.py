T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = [0] * 10
    for i in range(6):
        card[N % 10] += 1
        N //= 10

    run = tri = 0
    i = 0
    while i < 10:
        if card[i] >= 3:
            card[i] -= 3
            run += 1
            continue
        if card[i] >= 1 and card[i+1] >=1 and card[i+2] >=1:
            card[i] -= 1
            card[i+1] -= 1
            card[i+2] -= 1
            tri += 1
            continue
        i += 1
    if run + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
