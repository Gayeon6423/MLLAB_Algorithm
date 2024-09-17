def solution(elements):
    answer = 0
    elements_twice = elements * 2 
    
    prefix_sum = [0] * len(elements_twice)
    prefix_sum[0] = elements_twice[0]
    for i in range(1,len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i - 1] + elements_twice[i]
    num_set = set()
    for subset_length in range(1, len(elements)+1):
        for subset in range(len(elements)):
            sum = prefix_sum[subset + subset_length] - prefix_sum[subset]
            num_set.add(sum)
    answer = len(num_set)
    return answer