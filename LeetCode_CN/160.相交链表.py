#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        indexA = headA
        indexB = headB
        while indexA != indexB:
            if indexA == None:
                indexA = headB
            else:
                indexA = indexA.next

            if indexB == None:
                indexB = headA
            else:
                indexB = indexB.next
        return indexA
        
# @lc code=end

