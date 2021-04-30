
def dfs(start, num_list, add, sub, mul, div, result):
    if start == len(num_list):
        global min_
        global max_

        min_ = min(result, min_)
        max_ = max(result, max_)

    if add :
        dfs(start+1, num_list, add-1, sub, mul, div, result + num_list[start])

    if sub :
        dfs(start+1, num_list, add, sub-1, mul, div, result- num_list[start])
    
    if mul :
        dfs(start+1, num_list, add, sub, mul-1, div, result * num_list[start])
    
    if div :
        dfs(start+1, num_list, add, sub, mul, div-1, int(result / num_list[start]))

    return result
    


if __name__ == "__main__":
    min_, max_ = float('inf'), -float('inf')    
    _ = int(input())
    num_list=list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    dfs(1, num_list, add, sub, mul, div, num_list[0])
    print(max_)
    print(min_)