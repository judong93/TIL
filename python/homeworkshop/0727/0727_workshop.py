''' 1번 문제 내가 한것.
def get_dict_avg(dict_a):
    total = 0
    cnt = 0
    for name in dict_a:
        total += dict_a[name]
        cnt += 1
    return total / cnt

print(get_dict_avg({
    'python': 80, 
    'algorithm': 90, 
    'django': 89, 
    'web': 83
}))
'''
''' 교수님 1번
def get_dict_avg(scores):
    total = 0
    for score in scores.values():
        total += score
    
    return total / len(scores)

print(get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83
}))
'''

# 2번째 문제. 내가 한 것.
def count_blood(type_list):
    new_dict = {'A': 0, 'B': 0, 'O': 0, 'AB': 0}
    for blood_type in new_dict:
        new_dict[blood_type] = type_list.count(blood_type)
    return new_dict

print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']))


'''
def count_blood(blood_list):
    result_dict = {}
    for blood in blood_list:
        #.get()을 통해 값이 있으면 <기존값 +1>
        # 값이 없으면 <0+1>
        result_dict[blood] = result_dict.get(blood, 0) + 1
    return result_dict

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB' 
]))
'''

'''
    for blood in blood_list:
        if blood in result_dict:
            result_dict[blood] += 1
        
        else:
            result_dict[blood] = 1
    return result_dict
'''