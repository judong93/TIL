T = int(input())
for tc in range(1, T+1):
    part = input()
    text = input()
    max_val = 0
    for i in part:
        cnt = 0
        for j in text:
            if i == j:
               cnt += 1
        if max_val < cnt:
            max_val = cnt
    print(f'#{tc} {max_val}')
