#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        indexR = length - 1
        for indexL in range(length // 2):
            temp = s[indexL]
            s[indexL] = s[indexR - indexL]
            s[indexR - indexL] = temp
# @lc code=end

