class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1List = []
        l2List = []

        Headl1 = l1
        Headl2 = l2

        while(Headl1 != None):
            l1List.append(Headl1.val)
            Headl1 = Headl1.next

        while(Headl2 != None):
            l2List.append(Headl2.val)
            Headl2 = Headl2.next

        l1List.reverse()
        l2List.reverse()
        
        L1Number = int("".join(map(str, l1List))) if l1List else 0
        L2Number = int("".join(map(str, l2List))) if l2List else 0

        Sum = L1Number + L2Number

        StringSum = str(Sum)
        ReversedStringSum = StringSum[::-1]

        returnHead = None
        current = None

        for i in ReversedStringSum:
            new_node = ListNode(int(i))
            if(returnHead == None):
                returnHead = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node

        return returnHead