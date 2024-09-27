#Finding the maximum number of a list using Divide and Conquer(Recursive) method
def find_max_recursive(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        mid = len(nums) // 2
        left_max = find_max_recursive(nums[:mid])
        right_max = find_max_recursive(nums[mid:])
        return max(left_max, right_max)
#Example
list = [2, 5, 10, 1, 3, 12, 4, 9]
print(find_max_recursive(list))