"""
문제 이름: 신고 결과 받기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""

# 통과한 코드 (내 풀이))
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    singo = {}
    # 신고당한 아이디를 key, 신고한 아이디를 value로.
    for rp in report:
        value, key = rp.split()
        singo.setdefault(key, set())
        singo[key].add(value)

    for _, val in singo.items():
        if len(val) >= k:
            for v in val:
                idx = id_list.index(v)
                answer[idx] += 1
    return answer


"""
setdefault를 사용했는데, 사실 가독성을 위해서는 아래처럼 작성하는게 더 나을 수도 있겠다.
    if key not in singo:
        singo[key] = set()
    singo[key].add(value)
    
그리고 setdefault의 단점이 있는데, 이미 존재하는 key에 대해서도 함수가 호출되어 오버헤드가 발생할 수 있다고 한다.
"""
