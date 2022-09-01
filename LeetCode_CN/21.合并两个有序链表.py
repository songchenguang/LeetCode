#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        index1 = head = list1 if list1.val < list2.val else list2
        index2 = list1 if head is list2 else list2
        while index1:
            if index1.next == None:
                index1.next = index2
                break
            elif index2 == None:
                break
            elif index1.next.val < index2.val:
                index1 = index1.next
            elif index1.next.val >= index2.val:
                temp = index2
                index2 = index2.next
                temp.next = index1.next
                index1.next = temp
        return head
    
# @lc code=end

