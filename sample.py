class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
def b(l1:ListNode, l2:ListNode) -> ListNode:
    dummy = first = ListNode(0)
    carry = 0
    while(l1 or l2 or carry):
        tot = carry
        if(l1):
            tot += l1.val
            l1 = l1.next
        if(l2):
            tot += l2.val
            l2 = l2.next
        carry = tot // 10
        tot = tot % 10
        dummy.next = Listnode(tot)
        dummy = dummy.next
    return(first.next)
    
