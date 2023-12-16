"""
문제 이름: 프로세스
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
"""

# 2, 5, 18 틀림
def solution(priorities, location):
    answer = 0
    # 관건: location의 프로세스를 어떻게 추적하는지
    # tuple?
    prior = []
    loc = []
    for i, p in enumerate(priorities):
        prior.append(p)
        loc.append(i==location)

    count = 0
    while(prior):
        if len(prior) == 1:
            break
        cur_p = prior[0]
        cur_l = loc[0]
        if cur_p >= max(prior[1:]):
            prior = prior[1:]
            loc = loc[1:]
            count += 1
            if cur_l == True:
                answer = count
                break
        else:
            prior = prior[1:] + [cur_p]
            loc = loc[1:] + [cur_l]
        
    return answer


# 통과한 코드 - prior len이 1일 때 count++를 해주면서 통과함
def solution(priorities, location):
    answer = 0
    prior = []
    loc = []
    for i, p in enumerate(priorities):
        prior.append(p)
        loc.append(i==location)

    count = 0
    while(prior):
        if len(prior) == 1:
            count += 1
            break
        cur_p = prior[0]
        cur_l = loc[0]
        if cur_p >= max(prior[1:]):
            prior = prior[1:]
            loc = loc[1:]
            count += 1
            if cur_l == True:
                answer = count
                break
        else:
            prior = prior[1:] + [cur_p]
            loc = loc[1:] + [cur_l]
    answer = count
    return answer