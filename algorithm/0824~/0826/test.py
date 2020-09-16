new_id = input()
def solution(new_id):
    N = len(new_id)
    oper = ['-', '_', '.']
    new_id = new_id.lower()  # 1단계
    new_id1 = ''
    for i in new_id:  # 2단계
        if i.islower() or i.isdigit() or i in oper:
            new_id1 += i

    N1 = len(new_id1)
    cnt = 0
    store = []
    new_id2 = list(new_id1)
    for i in range(N1): # 3단계
        if new_id1[i] == '.':
            cnt += 1
            if cnt == 2:
                store.append(i)
                cnt = 1
        else:
            cnt = 0

    for i in store[::-1]:
        new_id2.pop(i)

    if new_id2 and new_id2[0] == '.': # 4단계
        new_id2.pop(0)
    if new_id2 and new_id2[-1] == '.':
        new_id2.pop()
    new_id2 = ''.join(new_id2)

    if new_id2 == '': # 5단계
        new_id2 += 'a'

    if len(new_id2) >= 16: # 6단계
        new_id2 = new_id2[:15]
        new_id2 = list(new_id2)
        if new_id2[-1] == '.':
            new_id2.pop()
        new_id2 = ''.join(new_id2)

    if len(new_id2) <= 2:
        while len(new_id2) == 3:
            new_id2 += new_id2[-1]
    return new_id2
print(solution(new_id))
    # answer = new_id
    # return answer