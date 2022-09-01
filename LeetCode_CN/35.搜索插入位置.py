#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] == target:
                return index
            if index == len(nums) - 1 and nums[index] < target:
                return len(nums)
            if target > nums[index] and target < nums[index + 1]:
                return index + 1
        return 0
            
# @lc code=end

