# Input: nums = [1,2,4,6]
# prefix
# [1, 1, 2, 8]

# Sufix:
# [48 ,24 ,6 ,1]

# result = [1] * 4

# # Output: [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

