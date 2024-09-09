def solution(s):
    return " ".join([i.capitalize() if i != "" else i for i in s.split(" ")])