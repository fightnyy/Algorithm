from pdb import set_trace
def longestPalindrome(s: str) -> str:
    s = s.lower()
    left, right = 0, len(s)
    longest = s[0]
    while left < right :
        while right != left :
            # set_trace()
            tmp = s[left:right]
            if tmp == tmp[::-1] and len(longest) < right - left:
                longest = s[left:right]
            right -= 1
        right = len(s)
        left += 1
    return longest

print(longestPalindrome("cbbd"))