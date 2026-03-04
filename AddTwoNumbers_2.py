class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LtoLL:
    def ListToLinkedList(self, li):
        start = run = ListNode(0)
        for i in li:
            run.next = ListNode(i)
            run = run.next
        return(start.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        current = head
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            total = val1 + val2 + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next

class mainSol:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def addTwoNums(self):
        l1 = LtoLL().ListToLinkedList(self.l1)
        l2 = LtoLL().ListToLinkedList(self.l2)
        result = Solution().addTwoNumbers(l1, l2)
        l = []
        while result:
            l.append(result.val)
            result = result.next
        return(l)
    
def main(l1=[], l2=[]):
    obj1 = mainSol(l1,l2)
    obj2 = mainSol([2,5],[5,5])
    return(obj1.addTwoNums())
    
