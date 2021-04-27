import sys
import pdb

n = input()
len_n = len(n)
n = int(n)
cmp = n - (9 * len_n)
while cmp < 0:
    cmp += 1
while True:

    str_cmp = list(str(cmp))
    tmp_cmp = cmp
    # pdb.set_trace()
    for val in str_cmp:
        tmp_cmp += int(val)

    if tmp_cmp == n:
        print(cmp)
        sys.exit(0)
    if cmp > n:
        print(0)
        sys.exit(0)
    cmp += 1
print(n)
