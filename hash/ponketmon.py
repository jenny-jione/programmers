"""
폰켓몬
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""

def solution(nums):
    answer = 0
    p_dict = {}
    for n in nums:
        p_dict.setdefault(n, 0)
        p_dict[n] += 1
    answer = min(len(nums)/2, len(p_dict))
    return answer



"""
Review:
해시 분류에 있어서 dictionary를 사용했는데, 사실 내가 얻고자 한 것은 key의 개수였다. 
그러면 사실 value는 필요없기 때문에 dictionary를 사용할 이유가 없다.
단순하게 set(nums)를 적용해서 len만 구하면 코드가 훨씬 간결해진다.
"""