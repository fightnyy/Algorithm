import pdb

string = "babadasdeqwe"


def expand(left: int, right: int) -> str:
    while left >= 0 and right <= len(string) and string[left] == string[right - 1]:
        pdb.set_trace()
        left -= 1
        right += 1
    return string[left + 1 : right - 1]


if len(string) < 3 and string == string[::-1]:
    print("result: ", string)

result = ""
for i in range(len(string) - 1):

    result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
print("result : ", result)
