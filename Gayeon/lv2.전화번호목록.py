def solution(phone_bank):
    phone_check_li = []
    for i in range(len(phone_bank)):
        tmp = phone_bank[:i] + phone_bank[i+1:]
        phone_check_li.append(tmp)

    answer = 'ture'
    for index, phone in enumerate(phone_bank):
        for check in phone_check_li[index]:
            if phone in check[:len(phone)]:
                answer = 'false'
                break
    return answer

phone_bank = ["119", "97674223", "1195524421"]
solution(phone_bank)