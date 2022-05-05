from math import pow
"""
파이썬은 음수를 10으로 나눈 경우에 10으로 뺸 결과가 나머지가 되지만 
자바는 음수를 10으로 나눈 경우에 상관없이 -1이 됩니다.
예를 들어 자바를 -123 을 % 10 으로 한 경우에 3 이 되지만
파이썬은 -123 을 % 10 으로 한 경우에 7이 됩니다.
"""
class Solution:
    def reverse(self, x: int) -> int:
        postive_int_max_size = pow(2, 31) - 1
        negative_int_max_size = pow(-2, 31)
        result = 0
        figure = 1
        if (x < 0):
            x = x * -1
            figure = -1
        while x > 0:
            pop = x % 10 
            x //= 10
            if result * 10 + pop > postive_int_max_size :
                return 0
            if result * 10 + pop < negative_int_max_size :
                return 0
            
            result = 10 * result + pop
        return result * figure
        
#         if x > 0:
#             list_int=list(str(x))
#             list_int=list_int[::-1]
#             str_int="".join(list_int)
#             result = int(str_int)
#             if result > pow(2,31) - 1:
#                 return 0
#             return result
#         else:
#             x = x *-1
#             list_int=list(str(x))
#             list_int=list_int[::-1]
#             str_int="".join(list_int)
#             result = int(str_int) * -1
#             if result < pow(-2,31):
#                 return 0
#             return result
            