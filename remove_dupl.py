# Здесь было всё очень страшно, и я переделал всё с корнями. Надеюсь, не напортацил ещё больше

def remove_duplicates(nums: list[int]) -> None:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
        

nums = [1, 1, 2]
remove_duplicates(nums)
assert nums == [1, 2]

nums = [0,0,1,1,1,2,2,3,3,4]
remove_duplicates(nums)
assert nums == [0, 1, 2, 3, 4]

nums = [1, 2, 3]
remove_duplicates(nums)
assert nums == [1, 2, 3]

nums = [1, 1]
remove_duplicates(nums)
assert nums == [1]