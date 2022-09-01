#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        fast = head
        slow = newHead
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return newHead.next
        



# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         curr = head
#         linkedList = []
#         while curr:
#             linkedList.append(curr)
#             curr = curr.next
#         length = len(linkedList)
#         index = length - n
#         if index == 0:
#             return head.next
#         elif index == length - 1:
#             linkedList[index - 1].next = None
#             return head
#         else:
#             linkedList[index - 1].next = linkedList[index + 1]
#             return head


        
# @lc code=end

