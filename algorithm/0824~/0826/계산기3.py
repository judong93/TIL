for tc in range(1, 11):
    N = int(input())
    arr = input()
    oper = ['+', '*', '(']
    result = ''
    stack = []
    icp = {'(':0, '*':1, '+':2}
    isp = {'(':3, '*':1, '+':2}
    for i in arr:
        if i not in oper and i != ')':
            result += i
        elif i in oper:
            if not stack:
                stack.append(i)
            else:
                if icp[i] < isp[stack[-1]]:
                    stack.append(i)
                else:
                    while True:
                        if icp[i] < isp[stack[-1]]:
                            stack.append(i)
                            break
                        else:
                            result += stack.pop()
        elif i == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                else:
                    result += x # 첫번째 작업 끝(후위 표현식으로 완성)
    new_arr = []
    for i in result:
        if i.isdigit() == True:
            new_arr.append(int(i))
        else:
            a = new_arr.pop()
            b = new_arr.pop()
            if i == '+':
                new_arr.append(a+b)
            else:
                new_arr.append(a*b)
    print(f'#{tc} {new_arr[0]}')


