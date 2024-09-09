def solution(s):
    answer = True
    string = [i for i in s]
    count = 0
    for i in string:
        if i == "(":
            count+=1
        if i == ")":
            count-=1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False