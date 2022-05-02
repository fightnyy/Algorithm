import re


def isPalindrome(s: str):
    s = s.lower()
    s = re.sub("[^a-zA-Z0-9]", "", s)
    return s == s[::-1]
