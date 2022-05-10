from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result =[]
        self.helper([],1,k,n)
        return self.result
    
    def helper(self,path,start,k,target):
        print(path)
        if k ==0 and target==0:
            
            self.result.append(path)
            return 
        
        if k ==0 or target==0:
            return
        
        for i in range(start,10):
            self.helper(path+[i],i+1,k-1,target-i)





from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num_list = [1,2,3,4,5,6,7,8,9]
        answer = []
        
        def _backtrack(index, candidate):
            print(candidate)
            if len(candidate) == k and sum(candidate) == n:
                answer.append(candidate)
                return
            if len(candidate) == k or sum(candidate) == n:
                return
            
            for idx, num in enumerate(num_list[index:]):
                _backtrack(idx + 1, candidate + [num])
        _backtrack(0, [])
        return list(answer)


s = Solution()
print(s.combinationSum3(3, 7))