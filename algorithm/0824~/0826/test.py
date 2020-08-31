for _ in range(10):
    N = int(input())
    text = input()
    stack = []
    result = ''
    com = {'(':0, '+':2, '-':2, '*':1, '/':1}
    sta = {'(':3, '+':2, '-':2, '*':1, '/':1}
    oper = ['(','+','-','*','/']
    for i in text:
        if i in oper:
            if stack and sta[stack[-1]] >= com[i]:
                while sta[stack[-1]] < com[i]:
                    stack.pop()
            stack.append(i)
        elif i == ')':
            while stack[-1] == '(':
                stack.pop()
            stack.pop()
        else:
            stack.append(i)