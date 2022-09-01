#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = 0
#         while index < len(nums) - 1:
#             if nums[index] in nums[(index + 1):]:
#                 nums.pop(index)
#             else:
#                 index += 1
#         return len(nums)
    
            
# @lc code=end

