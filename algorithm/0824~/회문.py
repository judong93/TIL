T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    text = [input() for _ in range(n)]
    for i in range(n): # 리스트 내 글자로 접근
        for j in range(n - m + 1): # 회문의 길이가 충족되는 시작점까지만 순환.
            cnt = 0
            for k in range(m // 2): # 회문 길이의 절반만큼만 순환
                if text[i][j+k] == text[i][j+m-k-1]:  # 양 끝점에서 하나씩 안으로 이동하며 비교.
                    cnt += 1
                else: #하나라도 틀리면 브레이크
                    break
            if cnt == m // 2:
                palin = text[i] #회문을 찾았으므로 변수 지정.
                print(f'#{tc} {palin[j:j+m]}')
                break

            for l in range(m // 2):
                if text[j+l][i] == text[j+m-l-1][i]:
                    cnt += 1
                else:
                    break

            if cnt == m // 2:
                result = ''
                for x in range(m):
                    result += text[j+x][i]
                print(f'#{tc} {result}')

