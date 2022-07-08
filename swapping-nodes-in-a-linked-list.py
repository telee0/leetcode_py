# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_prev = ListNode()
        head_prev.next = head

        node = head
        prev = head_prev
        n = 0
        while node:
            n += 1
            if n == k:
                nodeA = node
                prevA = prev
                nodeB = head
                prevB = head_prev
            elif n > k:
                prevB = nodeB
                nodeB = nodeB.next
            prev = node
            node = node.next

        # print("n =", n)

        if nodeA == nodeB:
            return head
        elif nodeA.next == nodeB:
            prevA.next = nodeB
            nodeA.next = nodeB.next
            nodeB.next = nodeA
        elif nodeB.next == nodeA:
            prevB.next = nodeA
            nodeB.next = nodeA.next
            nodeA.next = nodeB
        else:
            temp = nodeA.next
            nodeA.next = nodeB.next
            nodeB.next = temp
            temp = prevA.next
            prevA.next = prevB.next
            prevB.next = temp

        if head == nodeA:
            head = nodeB
        elif head == nodeB:
            head = nodeA

        return head

