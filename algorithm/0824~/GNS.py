s = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T + 1):
    tcs, num = input().split()
    N = int(num)
    arr = list(input().split())
    cnt = [0] * 10
    for x in arr:
        if x == 'ZRO':
            cnt[0] += 1
        elif x == 'ONE':
            cnt[1] += 1
        elif x == 'TWO':
            cnt[2] += 1
        elif x == 'THR':
            cnt[3] += 1
        elif x == 'FOR':
            cnt[4] += 1
        elif x == 'FIV':
            cnt[5] += 1
        elif x == 'SIX':
            cnt[6] += 1
        elif x == 'SVN':
            cnt[7] += 1
        elif x == 'EGT':
            cnt[8] += 1
        elif x == 'NIN':
            cnt[9] += 1
    print(tcs)
    for i in range(10):
        for j in range(cnt[i]):
            print(s[i], end=' ')