from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for c in sorted_counter:
        answer += 1
        k -= c[1]
        if k<=0: break
    return answer