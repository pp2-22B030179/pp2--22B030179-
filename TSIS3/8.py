def spy_game(nums):
    code = [0, 0, 7, 'a']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return code==['a']

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))