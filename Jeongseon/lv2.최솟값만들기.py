def solution(A, B):
    A = sorted(A, reverse = False)
    B = sorted(B, reverse = True)
    c = [a*b for a, b in zip(A, B)]

    answer = sum(c)
    return answer
