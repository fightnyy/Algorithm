from typing import List
phone_dict = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
product_list = []
def letterCombinations(digits: str) -> List[str]:    
    backtrack(digits, 0, "")
    print(product_list)
def backtrack(digits, index, letter):
    if index == len(digits):
        product_list.append(letter)
        return;
    num = digits[index]
    string = phone_dict[num]
    
    for char in string:
        backtrack(digits, index+1, letter+char)

if __name__ == "__main__":
    letterCombinations('23')
