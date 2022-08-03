def solution(estimates, k):
    current_sum = sum(estimates[0:k])
    max_sum = current_sum
    
    for i in range(len(estimates)-k):
        current_sum = current_sum - estimates[i] + estimates[i+k]
        max_sum = max(max_sum, current_sum)
    return max_sum