def backspaceCompare(s:str, t:str):
    s_stack = []
    t_stack = []
    for char in s:
        if char == '#':
            s_stack.pop()
        else:
            s_stack.append(char)
    for char in t:
        if char == '#':
            t_stack.pop()
        else:
            t_stack.append(char)
    s = "".join(s_stack)
    t = "".join(t_stack)

    return s == t