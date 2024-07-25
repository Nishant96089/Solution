class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Solution:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def traverse_and_print(self):
        temp = self.head
        while temp:
            print(temp.data,end=" => ")
            temp = temp.next
        print("None")
        
    def addition(self):
        sum = 0
        current = self.head
        while current is not None:
            sum = sum + current.data
            current = current.next
        return sum
        
    def subtraction(self):
        current = self.head.next
        ans = current.data
        while current is not None:
            ans = ans - current.data
            current = current.next
        return ans
        
    def multiplication(self):
        ans = 1
        current = self.head
        while current is not None:
            ans = ans * current.data
            current = current.next
        return ans    
            
                
        
LL = Solution()
elements = int(input("Enter the number of elemnts you want: "))
for _ in range(elements):
    n = int(input("Enter element: "))
    LL.insert(n)
    
LL.traverse_and_print()
print(LL.addition())
print(LL.subtraction())
print(LL.multiplication())
