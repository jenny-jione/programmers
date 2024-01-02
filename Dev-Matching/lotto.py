"""
문제 이름: 로또의 최고 순위와 최저 순위
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77484

타임라인
24.01.02 7:55pm~8:07pm
"""

def solution(lottos, win_nums):
    answer = [0] * 2
    hit = 0
    possible = lottos.count(0)
    for wn in win_nums:
        if wn in lottos:
            hit += 1
    if hit > 1:
        min_rank = 7 - hit
    else:
        min_rank = 6
    if min_rank - possible < 1:
        max_rank = 1
    else:
        max_rank = min_rank - possible
    answer[0] = max_rank
    answer[1] = min_rank
    return answer


"""
사용한 개념
1) 0으로 초기화하는 리스트
2) 리스트의 특정 요소 개수 세기. li.count(요소)


다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0+ans], rank[ans]

인덱스로 접근하는 부분이 좋은 것 같다..
"""