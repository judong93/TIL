T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    oper = ['+', '-', '*', '/']
    result = 'error'
    for i in arr:
        if i not in oper and i != '.': # 정수일때
            stack.append(int(i))
        elif i in oper and len(stack) >= 2: #연산자고, 스택이 2이상
            o, t = stack.pop(-2), stack.pop()
            if i == oper[0]:
                stack.append(o + t)
            elif i == oper[1]:
                stack.append(o-t)
            elif i == oper[2]:
                stack.append(o*t)
            elif i == oper[3]:
                stack.append(o/t)
        elif i == '.' and len(stack) == 1: # '.' 이고 스택에 한개일 떄
            result = stack[0]
        else:
            break
    print(f'#{tc} {result}')