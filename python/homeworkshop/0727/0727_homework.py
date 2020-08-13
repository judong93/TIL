# 내가 푼 것. 1번
def count_vowels(name):
    vowel = 'aeiou'
    cnt = 0
    for char in name:
        if char in vowel:
            cnt += 1
    return cnt

print(count_vowels('apple'))
print(count_vowels('banana'))



# 내가 푼 것 2번
def only_square_area(a, b):
    total = []
    for num_a in a:
        for num_b in b:
            if num_a == num_b:
                total.append(num_a * num_b)
    return total
    

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
