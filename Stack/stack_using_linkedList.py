# Element class
class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

# LinkedList class to implement Stack
class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	# Insert at head of the LinkedList
	def insert_first(self, newElement):
		newElement.next = self.head
		self.head = newElement
	
	# Delete from the head of the LinkedList
	def delete_first(self):
		if self.head:
			deletedItem = self.head
			self.head = deletedItem.next
			return deletedItem
		else:
			return None
	
# Stack class
class Stack(object):
	def __init__(self,top = None):
		self.ll = LinkedList(top)
	
	# Push newElement into Stack
	def push(self, newElement):
		self.ll.insert_first(newElement)
	
	# Pop element at the head/top of the Stack
	def pop(self):
		return self.ll.delete_first()

# Set up some elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Initialize the Stack
stack = Stack()

# Push into Stack
stack.push(e1)
stack.push(e2)
stack.push(e3)
stack.push(e4)

# Pop from stack and print
print(stack.pop().value) # print 4
print(stack.pop().value) # print 3


