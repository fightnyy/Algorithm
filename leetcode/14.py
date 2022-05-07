class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(sorted(strs, key=lambda x: len(x))[0])
        if min_len == 0:
            return ""
        past = strs[0]
        return self.make_answer(strs, min_len, past)

    def make_answer(self, strs, min_len, past):
        r_idx = 0
        for idx in range(0, min_len):
            for string in strs:
                if string[:idx+1] == past[:idx+1]:
                    past = string
                    r_idx = idx
                    continue 
                else : 
                    return past[:idx]
        return past[:r_idx+1]



    def longestCommonPrefixSolution1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 


    def longestCommonPrefixSolution2(self, strs):
        longest_pre = ""
        if not strs: return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break
        return longest_pre