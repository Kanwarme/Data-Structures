class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None
class Stack:
	def __init__(self):
		self.head = Node()
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	def pop(self):
		if(self.isEmpty()):
			return float("-inf")
		temp = self.head
		self.head = self.head.next
		return temp.data

	def peek(self):
		return self.head.data

	def isEmpty(self):
		return True if self.head is None else False


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack.pop())
print(stack.peek())