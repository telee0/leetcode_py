"""

https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node:
            if node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                node = node.next

        return head