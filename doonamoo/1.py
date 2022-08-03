
def solution(estimates, k):
    max_result = sum(estimates[0:k])
    for i in range(len(estimates)):
        tmp_result = sum(estimates[i:i+k])

        # if max_result < tmp_result:
        #     max_result=tmp_result
        #     answer = estimates[i : i+k]
        max_result = max(max_result, tmp_result)


    return max_result

estimates = [5,1,9,8,10,5]
k = 3

estimates = [10, 1, 10, 1, 1, 4, 3, 10]
k = 6
print(solution(estimates, k))