"""
의상
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

def solution(clothes):
    answer = 1
    kind = {}
    for c in clothes:
        kind.setdefault(c[1], 0)
        kind[c[1]] += 1
    for v in kind.values():
        answer *= (v+1)
    answer -= 1
    return answer


"""
map 등을 활용해서 리스트의 모든 요소에 +1을 더한 값을 곱해주는 방법이 있을 것 같은데.. 
일단 내 풀이는 위 코드가 최선이다.
"""