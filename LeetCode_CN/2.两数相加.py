#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start


# Definition for singly-linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num1 + num2 + carry
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

        return head.next
        
# @lc code=end

