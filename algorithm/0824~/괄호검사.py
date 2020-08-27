# 주동아! 스택에서 팝할 떄는 isEmpty를 꼭 체크하자! 안하고 내니까 런타임에러 떴잖니!!!!!!

def ins(t):
    stack = []
    for i in t:
        if i == '(' or  i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return 0
        elif i == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    t = input()
    result = ins(t)
    print(f'#{tc} {result}')
