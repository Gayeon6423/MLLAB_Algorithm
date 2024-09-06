def Collatz(k):
    value = []
    i = 0
    while k>1:
        value.append((i,k))
        if k%2==0:
            k = k//2
        else:
            k = 3 * k + 1
        i += 1
    value.append((i,k))
    return value
        

def solution(k, ranges):
    answer = []
    Collatz_list = Collatz(k)
    surface_list = []
    for i in range(1,len(Collatz_list)):
        surface_list.append((Collatz_list[i][1]+Collatz_list[i-1][1])/2)
    for interval in ranges:
        a = interval[0]
        b = len(Collatz_list) - 1 + interval[1]
        if a>b:
            answer.append(-1.0)
        elif a==b:
            answer.append(0.0)
        else:
            answer.append(sum(surface_list[a:b]))
    return answer