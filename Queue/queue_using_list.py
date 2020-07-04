class Queue(object):
        # intialize the queue with a List storage.
	def __init__(self, head=None):
		self.storage = [head]
		
        # add newElement at tail of the queue.
	def enqueue(self, newElement):
		self.storage.append(newElement)

	# peek the element at head of the queue.
	def peek(self):
		return self.storage[0]

	# remove and return element at head of the queue.
	def dequeue(self):
		return self.storage.pop(0)

# Initiate a queue and add elements to it.
q = Queue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

# Test peek
print(q.peek()) # print 0

# Test dequeue
print(q.dequeue()) # print 0
print(q.dequeue()) # print 1
print(q.dequeue()) # print 2


