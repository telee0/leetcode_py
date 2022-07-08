# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = ListNode()
        node = output

        node1 = list1
        node2 = list2

        while node1 and node2:
            if node1.val > node2.val:
                node.next = node2
                node2 = node2.next
            else:
                node.next = node1
                node1 = node1.next
            node = node.next

        if node1:
            node.next = node1
        elif node2:
            node.next = node2

        return output.next

sol = Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))
