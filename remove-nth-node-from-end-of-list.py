# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        sz = 0
        while node:
            sz += 1
            node = node.next

        i = sz - n + 1

        if i == 1:
            return head.next

        prev = head
        node = head
        while i > 1:
            prev = node
            node = node.next
            i -= 1

        prev.next = node.next

        return head

