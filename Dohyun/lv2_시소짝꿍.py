from collections import Counter
import math

def solution(weights):
    answer = 0
    dictionary = Counter(weights)
    for d in range(100,1001):
        if dictionary[d]>0:
            answer += dictionary[d] * (dictionary[d] - 1) //2
            answer += dictionary[d] * dictionary[d* 4 / 3]
            answer += dictionary[d] * dictionary[d* 4 / 2]
            answer += dictionary[d] * dictionary[d* 3 / 2]
    return answer

print(solution([100,180,360,100,270]))
