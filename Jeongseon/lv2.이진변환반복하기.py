def solution(s):
    _len = 0
    zero = 0
    count = 0

    while (x!="1"):
        x1="".join([i if i=="1" else ""for i in x])
        zero += (len(x) - len(x1))
        _len += len(x1)
        count += 1
        x = format(len(x1),"b")

    answer = [count, zero]

    return answer