from collections import Counter
from pdb import set_trace


def c(s, k):
    left = right = 0
    counts = Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1

        most_char_n = counts.most_common(1)[0][1]

        if right - most_char_n - left > k:
            counts[s[left]] -= 1
            left += 1

    return right - left


s = "AAABB"
t = 2
print(c(s, t))
