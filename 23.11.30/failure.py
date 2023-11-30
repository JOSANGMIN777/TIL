# 카카오코딩테스트 실패율 문제 난이도 1

def solution(N, stages):
    answer = []
    same_list = [0] * (N + 2)
    len_list = {}
    stages.sort()
    now = len(stages)
    for i in stages:
        same_list[i] += 1

    for i in range(1, N + 1):
        if now == 0:
            len_list[i] = 0
            continue
        len_list[i] = same_list[i] / now
        now -= same_list[i]
    print(len_list)
    return sorted(len_list, key=lambda x: len_list[x], reverse=True)

N = 5
stages = [2,1,2,6,2,4,3,3]
result = [3,4,2,1,5]
print(solution(5,stages))