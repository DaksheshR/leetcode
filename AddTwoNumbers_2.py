class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = []
        sum = 0
        carry = 0
        for i in range(max(len(l1),len(l2))):
            x = l1[i] if i < len(l1) else 0
            y = l2[i] if i < len(l2) else 0
            sum = x + y + carry
            carry = sum // 10
            l3.append(sum % 10)
        if(carry):
            l3.append(carry)
        return(l3)