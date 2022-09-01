#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for index in range(len(strs[0])):
            curChar = strs[0][index]
            for item in strs:
                if len(item) == index or item[index] != curChar:
                    return strs[0][0 : index]
        return strs[0]
# @lc code=end

