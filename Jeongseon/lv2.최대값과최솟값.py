def solution (s):
    nums = s.split(" ")
    nums = [int(num) for num in nums]
    _max = max(nums)
    _min = min(nums)
    answer = f"{_min:} {_max:}"
    return answer