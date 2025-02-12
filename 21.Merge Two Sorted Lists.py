# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head = ListNode() 
        temp = head  
        while list1 and list2 :
            if list1.val < list2.val :
                #直接設定temp = 那個Node
                temp.next = list1
                list1 = list1.next
            else :
                #直接設定temp = 那個Node
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next
        
        # 直接鏈接剩餘的節點，避免額外的 while 迴圈
        temp.next = list1 if list1 else list2

        return head.next # 跳過List的第一個Node.val = 0這個element
