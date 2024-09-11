def solution(n):
    count1=format(n, 'b').count('1')
    m=n+1
    while True:
        count2=format(m,'b').count('1')
        if count2 == count1:
            break
        else:
            m+=1
    return m