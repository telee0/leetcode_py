"""

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head

        prev, node = dummy, head
        val = head.val - 1

        while node:
            if node.next and node.val == node.next.val:
                val = node.val
                prev.next = node.next.next
                node = node.next.next
            elif node.val == val:
                prev.next = node.next
                node = node.next
            else:
                val = node.val
                prev = node
                node = node.next

        return dummy.next


sol = Solution()
