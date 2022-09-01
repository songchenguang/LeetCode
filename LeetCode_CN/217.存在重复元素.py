#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = dict()
        for item in nums:
            if item in numDict:
                return True
            else:
                numDict[item] = 1
        return False
# @lc code=end

