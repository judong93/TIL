def dele(text):
    if len(text) >= 2:
        for i in range(len(text)-1):
            if text[i] == text[i+1]:
                text.pop(i)
                text.pop(i)
                return dele(text)
    return len(text)

T = int(input())
for tc in range(1, T+1):
    text = list(input())
    result = dele(text)
    print(f'#{tc} {result}')
