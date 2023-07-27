# []

# 결과 => {'A': 3, 'B': 3, 'O' : 3. 'AB' : 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B','O','B','AB']
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_types in new_dict:
        # 기존에 키의 값을 +1 증가
        new_dict[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 설정되는 키) 키가 1로 설정되어야함
    else:
        new_dict[blood_type] = 1
print(new_dict)


# .get() if else대체 가능한 메서드

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B','O','B','AB']
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    
   new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)
    
'''    # 기존에 키가 이미 존재한다면,
    if blood_types in new_dict:
        # 기존에 키의 값을 +1 증가
        new_dict[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 설정되는 키) 키가 1로 설정되어야함
    else:
        new_dict[blood_type] = 1'''


# .setdefault()
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B','O','B','AB']
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
    print(new_dict)
    
    
    
    
    
