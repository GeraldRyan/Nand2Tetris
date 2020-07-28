class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Can create a hash table and check for existence or can create a counter for each item. Can create a dictionary with a key for the item and a counter for the number 
        tally = {}       
        for l in nums:
            if l in tally:
                return True
            else: 
                tally[l] = 'present'
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # Get a from l1
        num_strA = ""; num_strB = ""
        while l1.next is not None:
            num_strA = str(l1.val) + num_strA
            # Push to front of list
            l1 = l1.next
        num_strA = str(l1.val) + num_strA
        while l2.next is not None:
            num_strB = str(l2.val) + num_strB
            # Push to front of list
            l2 = l2.next
        num_strB = str(l2.val) + num_strB
        
        print(f"hello world {num_strA} plus {num_strB}")
        
        c = str(int(num_strA) + int(num_strB))
        print(f"The total should be {c}")
        
        # Put answer it back into LL format
        cur = dummy = ListNode(0)
        for char in reversed(c):
            cur.next = ListNode(char)
            cur = cur.next
    
        return dummy.next

    # I believe using string format for integer allows us to use Python for loop (for each loop)
    
    
    # get b from l2
    # get c = sum a + b
    # return digits of c into linked list as l1 and l2 
    # I believe using string format for integer allows us to use Python for loop (for each loop)
    
    
    # get b from l2
    # get c = sum a + b
    # return digits of c into linked list as l1 and l2 


class Solution:
    dex = 0
    values = {}
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        while cur.next is not None:
            if cur.val in self.values:
                return cur
            else:
                self.values[cur.val] = self.dex
            self.dex += 1
            cur = cur.next
        return null