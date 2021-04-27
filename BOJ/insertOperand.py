from itertools import permutations


def solve(num_list, op_list):
    operands = []
    for idx, val in enumerate(op_list):
        #         import pdb;pdb.set_trace()
        print(f"idx : {idx}, val : {val}")
        tmp = None
        if idx == 0:
            tmp = "+" * val
            operands.append(tmp)
        elif idx == 1:
            tmp = "-" * val
            operands.append(tmp)
        elif idx == 2:
            tmp = "*" * val
            operands.append(tmp)
        else:
            tmp = "//" * val
            operands.append(tmp)
    operands = "".join(operands)
    cnd = list(permutations(operands, len(num_list) - 1))
    high = -float("inf")
    low = float("inf")
    for c in cnd:
        tmp = ""
        answer = num_list[:]
        for idx in range(1, len(num_list)):
            answer.insert(2 * idx - 1, c[idx - 1])
        try:
            tmp = "".join(answer)
            print(tmp)
            # import pdb;pdb.set_trace()
            result = eval(tmp)
        except:
            import pdb

            pdb.set_trace()
        high = max(high, result)
        low = min(low, result)

    return high, low


if __name__ == "__main__":
    size = int(input())
    num_list = input().split()
    op_list = list(map(int, input().split()))
    high, low = solve(num_list, op_list)
    print(high)
    print(low)
