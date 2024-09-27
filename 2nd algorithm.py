#Finding the maximum of a list Using a For Loop
def find_max_loop(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
#Example
list = [2, 5, 10, 1, 3, 12, 4, 9]
print(find_max_loop(list))