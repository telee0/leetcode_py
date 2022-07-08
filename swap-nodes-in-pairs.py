# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        node = head
        if head.next:
            head = head.next
        prev = ListNode()

        while node:
            nodeA = node
            nodeB = nodeA.next
            if nodeB:
                nodeA.next = nodeB.next
                nodeB.next = nodeA
                node = nodeA.next
                prev.next = nodeB
                prev = nodeA
            else:
                break

        return head
