def solution(n, s):
    di = s // n
    re = s % n
    result = [di] * n
    if n > s:
        return [-1]
    elif re ==0 :
        return [di] * n
    else :
        for i in range(re):
            result[-(i+1)] += 1
        return result
            
        
        
        