from itertools import combinations
class Solution:
    def countVowelStrings(self, n: int) -> int:
        result = []
        vowel = 'aeiou'
        
        def backtrack(index, letter):
            if len(letter) == n :
                result.append(letter)
                return
            
            for idx in range(index, len(vowel)):
                backtrack(idx, letter + vowel[index])
                
        backtrack(0, '')
        return len(result)
        
class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        while (n) :
            o += u
            i += o
            e += i
            a += e
            n -= 1
        return a