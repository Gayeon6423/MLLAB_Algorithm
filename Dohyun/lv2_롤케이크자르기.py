from collections import Counter

def solution(topping):
    answer = 0
    one = Counter(topping)
    two = dict()
    for top in topping:
        if one[top]:
            one[top] -= 1
            if one[top]==0:
                del one[top]
            if top not in two.keys():
                two[top] = 1
            else:
                two[top] += 1
        if len(one.keys()) == len(two.keys()):
            answer += 1
    return answer