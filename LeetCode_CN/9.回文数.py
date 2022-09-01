#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
from operator import index


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        numList = []
        while x > 0:
            numList.append(x % 10)
            x = x // 10
        indexL = 0
        indexR = len(numList) - 1
        while indexL < indexR:
            if numList[indexL] != numList[indexR]:
                return False
            indexL += 1
            indexR -= 1
        return True
# @lc code=end

