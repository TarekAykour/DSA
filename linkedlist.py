# kids
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

# parent
class LinkedList:
    
    # traverse
    def traversal(self):
        first = self.head #set first to head of the linkedlist
        while first:
            print(first.data)
            first = first.next
    
    # insert
    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
    
    # search
    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False
        
    # delete
    def delete(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next #skipping node, by replacing it
        
    # delete tail
    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Abdulkadir")



family.head.next = wife #family head (the dad) points to the wife
wife.next = first_kid #wife points to first child
first_kid.next = second_kid #first child points to second child


family.insert_new_header("Dave")
family.delete("Bob")
family.delete_tail()
family.traversal()
# print(family.search("Bob"))