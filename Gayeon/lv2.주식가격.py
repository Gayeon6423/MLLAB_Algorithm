# 가격이 떨어지지 않은 기간 몇초인지 구하기

# solution1
def solution(prices):
    price_time = []
    time = 0
    for index, price in enumerate(prices):
        small_price = [x for x in prices[index+1:] if price > x] # 현재 주가보다 낮은 주가들
        # print('small:',small_price)
        if small_price: # 떨어진 주가 있다면
            small_price_index = index + prices[index+1:].index(small_price[0]) + 1# 떨어진 주가의 인덱스
            time = small_price_index - index  # 떨어지지 않은 기간
        else: # 떨어진 주가 없다면
            time = len(prices) - index - 1 # 떨어지지 않은 기간
        price_time.append(time)
        # print('price_time:',price_time)
    return price_time
    
prices = [1, 2, 3, 2, 3]
solution(prices)

# solution2
from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        time = 0
        price = prices.popleft()
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)



    