class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l3 = dummy
        while(l1 or l2):
            v1 = l1.val if l1 else 101
            v2 = l2.val if l2 else 101
            if v1==v2:
                l3.next = ListNode(v1)
                l3.next.next =ListNode(v2)
                l3 = l3.next.next
                l1 = l1.next
                l2 = l2.next
            elif v1<v2:
                l3.next = ListNode(v1)
                l3 = l3.next
                l1 = l1.next
            elif v2<v1:
                l3.next = ListNode(v2)
                l3 = l3.next
                l2 = l2.next
        return dummy.next
