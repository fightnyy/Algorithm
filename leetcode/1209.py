def removeDuplicates(s: str, k: int) -> str:
    flag = True
    stack = -1
    cnt = 0
    while flag:
        for idx, char in enumerate(s):
            if stack == char:
                cnt += 1
            else :
                cnt = 0

            if cnt == k-1:
                str_list = list(s)
                for jdx in range(idx-cnt, idx+1):
                    str_list[jdx] = ""
                    s = "".join(str_list)
                stack = -1
                cnt = 0
                break
            stack = char
        else:
            return s
    
s = "pbbcggttciiippooaais"
# s = "aabbccdde"
k = 2
print(removeDuplicates(s, k))