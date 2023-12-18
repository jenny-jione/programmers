"""
문제 이름: 이모티콘 할인 행사
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150368
"""


from itertools import product

def solution(users, emoticons):
    answer = [0, 0]    
    sale = [10, 20, 30, 40]

    combinations = product(sale, repeat=len(emoticons))

    for discount in combinations:
        emoticon_plus = 0
        total_sales = 0
        # 하나의 유저에 대해
        for user in users:
            user_pay = 0
            for i in range(len(discount)):
                # 유저가 설정한 할인율보다 제시한 할인율이 더 높은 이모티콘 모두 구매
                if user[0] <= discount[i]:
                    user_pay += int(emoticons[i] * (100-discount[i]) / 100)
                if user_pay >= user[1]:
                    break
            # 만약 제한금액을 넘어간다면 이모티콘 플러스 가입 & 구입은 취소
            if user_pay >= user[1]:
                emoticon_plus += 1
                user_pay = 0
            total_sales += user_pay
        
        # 현재까지의 이모티콘 플러스 가입자의 최댓값 구하기 (목표 1)
        if answer[0] < emoticon_plus:
            answer = [emoticon_plus, total_sales]
        # 이모티콘 플러스 가입자가 같다면 판매액의 최댓값으로 갱신하기 (목표 2)
        elif answer[0] == emoticon_plus:
            if answer[1] < total_sales:
                answer = [emoticon_plus, total_sales]
        
    return answer


"""
<새로 배운 것>
1. itertools.product -> 두개 이상의 리스트에 대해 모든 조합 구하기
"""