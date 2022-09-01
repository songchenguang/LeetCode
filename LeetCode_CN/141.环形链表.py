#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        fast = head
        slow = head
        
        while slow != None and fast != None:
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# @lc code=end

