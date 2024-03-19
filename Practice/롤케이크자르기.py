"""
문제 이름: 롤케이크 자르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265

타임라인
2024.3.19 14:40pm~
"""

def solution(topping):
    answer = -1
    dic1 = {}
    for t in topping:
        dic1.setdefault(t, 0)
        dic1[t] += 1
    
    dic2 = {}
    for t in topping:
        dic2.setdefault(t, 0)
        dic2[t] += 1
        dic1[t] -= 1
        if dic1[t] == 0:
            del(dic1[t])
        if len(dic2) == len(dic1):
            answer += 1
    return answer


"""
새로 배운 것
1. counter를 통해 리스트의 원소의 등장 횟수를 딕셔너리 형태로 저장할 수 있다.
2. dict에 pop이 있다. 물론 여기서는 필요 없음.
3. 추가되는 쪽은 굳이 dictionary일 필요가 없다. 토핑의 종류만 관리하면 되고, 각 종류가 몇 개씩 있느냐는 이 문제에서는 필요 없는 정보임.
    그래서 set으로 설정해도 된다.
"""
from collections import Counter

def solution(topping):
    answer = 0
    counter_dic = Counter(topping)
    set_dic = set()

    for t in topping:
        set_dic.add(t)
        counter_dic[t] -= 1
        if counter_dic[t] == 0:
            del(counter_dic[t])
        if len(counter_dic) == len(set_dic):
            answer += 1
    return answer