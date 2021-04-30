import sys
input = sys.stdin.readline
def solve(paren):
    stack = []
    for v in paren:
        if v == ']':
            t = 0
            while stack:
                top=stack.pop()
                if top == '[':
                    if t == 0:
                        t = 3
                    else :
                        t *= 3
                    stack.append(t)
                    break
                elif top == '(':
                    return 0
                else :
                    t+=top
    
            if not stack:
                return 0

        elif v == ')':
            t = 0
            while stack:
                top=stack.pop()
                if top == '(':
                    if t == 0:
                        t = 2
                    else :
                        t *= 2
                    stack.append(t)
                    break
                elif top == '[':
                    return 0
                else :
                    t+=top
            if not stack:
                return 0
        else :
            stack.append(v)
    try:
        stack=sum(stack)
    except :
        return 0
    return stack


if __name__ == '__main__':
    paren = input().rstrip()
    print(solve(list(paren)))