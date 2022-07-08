"""

https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.


https://www.geeksforgeeks.org/merge-sort/
https://www.geeksforgeeks.org/python-program-for-quicksort/

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeList(self, left, right):
        head = ListNode()
        node = head
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            node.next = left
        elif right:
            node.next = right
        return head.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.mergeList(left, right)
