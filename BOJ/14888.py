def solve(i,res, add, minus, mul, div):
    global max_, min_
    if i == size:
        
        max_ = max(max_, res)
        min_ = min(min_, res)
        return

    
    if add:
        solve(i+1, res+nums[i], add-1, minus, mul, div)
    if minus:
        solve(i+1, res-nums[i], add, minus-1, mul, div)
    if mul :
        solve(i+1, res*nums[i], add,minus, mul-1, div)
    if div :
        solve(i+1, int(res/nums[i]), add,minus, mul, div-1)



if __name__ == "__main__":
    size = int(input())
    nums = list(map(int, input().split()))
    max_ , min_ = -float('inf'), float('inf')
    add, minus, mul, div = map(int, input().split())
    solve(1,nums[0] , add, minus, mul, div)
    print(max_ , min_)