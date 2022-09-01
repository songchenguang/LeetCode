#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def checkBracket(self, s1: str, s2: str) -> bool:
        if s1 == '(' and s2 == ')':
            return True
        if s1 == '{' and s2 == '}':
            return True
        if s1 == '[' and s2 == ']':
            return True
        return False
    
    def isValid(self, s: str) -> bool:
        charList = []
        for index in range(len(s)):
            if len(charList) == 0:
                charList.append(s[index])
            elif self.checkBracket(charList[len(charList) - 1], s[index]):
                charList.pop()
            else:
                charList.append(s[index])
        if len(charList) == 0:
            return True
        else:
            return False
# @lc code=end

