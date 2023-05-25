# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = 0

        power = 0
        while(l1):
            ans += l1.val * pow(10, power)
            l1 = l1.next
            power += 1

        power = 0
        while(l2):
            ans += l2.val * pow(10, power)
            l2 = l2.next
            power += 1

        ans = str(ans)[::-1]

        head = ListNode(ans[0], None)
        current = head

        for i in range(1, len(ans)):
            current.next = ListNode(ans[i], None)
            current = current.next
        return head
