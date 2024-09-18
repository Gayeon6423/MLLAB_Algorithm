# solution1 : for문 활용
def solution(s):
    words = s.split(" ")
    tmp1 = []

    for word in words:
        tmp2 = []
        for i in range(len(word)):
            if i == 0:
                tmp2.append(word[i].upper())
            else:
                tmp2.append(word[i].lower())
        tmp1.append("".join(tmp2))
    return " ".join(tmp1)

s = "3people unFollowed me"
solution(s)

# solution2 : capitalize 활용
def solution(s):
    ans = ''
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize func : 첫 문자가 알파벳인 경우 대문자로, 두번째 문자부터 소문자로
        # 첫 문자 알파벳 아니면 그대로
        s[i] = s[i].capitalize()
    ans = ' '.join(s)
    return s

s = "3people unFollowed me"
solution(s)
