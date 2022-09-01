#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        newhead = index = ListNode(0, head)
        while index.next != None:
            if index.next.val == val:
                index.next = index.next.next
            else:
                index = index.next
                
        return newhead.next
# @lc code=end

