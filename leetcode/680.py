s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
def validPalindrome(s: str) -> bool:
    # 원래부터 palindrome 인 경우
    if s == s[::-1]:
        return True
    start, end = 0, len(s) - 1
    endure = 1
    
    for idx in range(len(s)//2):
        if s[idx+start] == s[end-idx] :
            continue
        else:
            import pdb;pdb.set_trace()
            if endure:
                endure -= 1
                if s[start+idx+1] == s[end-idx]:
                    start += 1
                    continue
                else:
                    if s[start+idx] == s[end-idx-1]:
                        end -= 1
                        continue
        return False
    return True
validPalindrome(s)