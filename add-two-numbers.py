"""

https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1.val
        l1 = l1.next
        pos = 10
        while l1:
            n1 = n1 + l1.val * pos
            l1 = l1.next
            pos *= 10

        n2 = l2.val
        l2 = l2.next
        pos = 10
        while l2:
            n2 = n2 + l2.val * pos
            l2 = l2.next
            pos *= 10

        sum = n1 + n2
        pos = 10

        head = ListNode()
        l3 = head

        for i in range(100):
            d = sum % 10
            sum = sum // 10
            l3.val = d
            if sum:
                l3.next = ListNode()
                l3 = l3.next
            else:
                break

        return head


"""
        ls = [int(x) for x in str(sum)]

        head = ListNode()
        l3 = head

        for i in range(len(ls) - 1, 1, -1):
            l3.val = ls[i]
            l3.next = ListNode()
            l3 = l3.next

        l3.val = l[0]

        return head
"""
"""
        head = ListNode()
        l3 = head
        up = 0

        for i in range(100):
            if l1:
                d1 = l1.val
                l1 = l1.next
            else:
                d1 = 0
            if l2:
                d2 = l2.val
                l2 = l2.next
            else:
                d2 = 0

            s = d1 + d2 + up
            up = s // 10

            l3.val = s % 10

            if l1 or l2:
                l3.next = ListNode()
                l3 = l3.next
            else:
                break

        if up > 0:
            l3.next = ListNode()
            l3.next.val = up

        return head
"""

"""
        l3 = []

        n1 = len(l1)
        n2 = len(l2)
        n = max(n1, n2)
        up = 0

        for i in range(n):
            d1 = l1[i] if i < n1 else 0
            d2 = l2[i] if i < n2 else 0
            s = d1 + d2 + up
            l3.append(s % 10)
            up = s // 10

        if up > 0:
            l3.append(up)

        return l3

solution = Solution()
print(solution.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

"""
