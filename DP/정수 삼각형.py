"""
문제 이름: 정수 삼각형
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
문제 티어: Lv.3

타임라인
2024.10.15 02:22pm~03:11pm (49분)  total: 49분

<정리>
1. dp
"""

def solution(tri):
    n = len(tri)
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = tri[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j==0:
                dp[i][0] = dp[i-1][0] + tri[i][0]
            elif j==i:
                dp[i][i] = dp[i-1][i-1] + tri[i][i]
            else:
                dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])