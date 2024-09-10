def solution(n):
    count = 0
    m = 1  # 연속된 숫자의 개수
    
    while m * (m - 1) // 2 < n:
        # n - m*(m-1)//2가 m의 배수인지 확인
        if (n - m * (m - 1) // 2) % m == 0:
            count += 1
        m += 1
    
    return count
