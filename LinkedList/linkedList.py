# Element class
class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

# LinkedList class
class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	# Print elements of the LinkedList
	def printList(self):
		current = self.head
		if self.head:
			while current.next:
				print(current.value)
				current = current.next
			print(current.value)
		else:
			print("List is empty.")
	
	# Append the newElement at last of the LinkedList
	def append(self, newElement):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = newElement
		else:
			self.head = newElement

	# Append the newElement at start/head of the LinkedList
	def insert_begin(self, newElement):
		newElement.next = self.head
		self.head = newElement
	
	# Insert the new node/element at a particular position (position start from 1)
	def insertAt(self, node, position):
		current_head = self.head
		pos = 1
		if position == 1:
			node.next = self.head
			self.head = node
		elif position > 1:
			while pos < position and current_head:
				if pos == position - 1:
					node.next = current_head.next
					current_head.next = node
					return
				if current_head.next == None and pos != position:
					return
				current_head = current_head.next
				pos += 1
		
	# Delete element from head of the LinkedList
	def delete_begin(self):
		if self.head:
			deletedItem = self.head
			self.head = deletedItem.next
			return deletedItem
		else:
			return None
	
	# Find and delete an element
	def delete(self, value):
		current_head = self.head 

		# if list is not initialized yet
		if current_head == None:
			return None
		# if value is the first node itself
		elif current_head.value == value:
			self.head = current_head.next
			current_head.next = None
		
		# other cases
		else:
			previous = current_head
			current_head = previous.next
			while current_head.value != value and current_head.next != None:
				previous = current_head
				current_head = current_head.next
			if(current_head.value == value):
				previous.next = current_head.next
				current_head.next = None
			
			# if item was not in the list
			else:
				return None

	# Get position of the element (position start from 1)
	def get_position(self, value):
		current_head = self.head
		position = 1
		if self.head == None:
			return None
		while current_head.value != value and current_head.next:
			position += 1
			current_head = current_head.next
		if current_head.next == None and current_head.value != value:
			return None
		else:
			return position
	
# New elements/nodes initialized
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# New LinkedList initialized
ll = LinkedList()

# Insertion of elements in List at various pos.
ll.append(e2)
ll.insert_begin(e1)
ll.insertAt(e3,3)
ll.append(e4)

# Print the list.
ll.printList()

# Get the position of a particular item in the list.
print(ll.get_position(4))
print(ll.get_position(1))

# Delete the items from List.
ll.delete_begin()
ll.delete(3)




