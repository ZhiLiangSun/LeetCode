# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 新增一個新的linked list -> cur(dummy)
        # 每次都指派較小值給cur.next，原linked list和cur會再往下移動一個
        # 做到最後一次比較後，利用"or"將剩下的最後一個加入到cur.next
        # 並return指向都不變的dummy.next
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


l1 = ListNode(1)
l2 = ListNode(3)
ans = Solution()
tmp = ans.mergeTwoLists(l1, l2)
