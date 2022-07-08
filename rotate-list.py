"""

https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

