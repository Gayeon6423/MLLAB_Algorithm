import math
from functools import reduce

def gcd_of_list(numbers):
    return reduce(math.gcd, numbers)

def solution(arrayA, arrayB):
    answer = 0
    while True:
        gcd_A = gcd_of_list(arrayA)
        gcd_B = gcd_of_list(arrayB)
        if arrayA == arrayB:
            answer = 0
            break        
        elif gcd_A != gcd_B:
            answer = -1
            if gcd_A > gcd_B:
                for ele in arrayB:
                    if ele % gcd_A == 0:
                        answer = 0
                        break
            else:
                for ele in arrayA:
                    if ele % gcd_B == 0:
                        answer = 0
                        break
            if answer !=0: answer = max(gcd_A, gcd_B)
            break
        elif gcd_A==1 or gcd_B==1:
            answer = 0
            break
    return answer
