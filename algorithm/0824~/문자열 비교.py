T= int(input())
for tc in range(1, T+1):
    part = input() # 패턴
    text = input() # 전체 글
    result = 0
    for i in range(len(text)- len(part) + 1):
        if text[i:i+len(part)] == part:
            result = 1
            break
    print(f'#{tc} {result}')
