class node:
	def __init__(self,data = None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self,):
		self.head = node()
	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next!= None:
			cur = cur.next
		cur.next = new_node
	def length(self):
		cur = self.head
		total = 0
		while cur.next!= None:
			total = total + 1
			cur = cur.next
		return total

	def display(self):
		elems = []
		cur_node = self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

def addNumbers(mylist1, mylist2):
	cur1 = mylist1.head
	cur2 = mylist2.head
	while cur1.next!=None:
		cur1 = cur1.next
		cur2 = cur2.next
		cur1.data = cur1.data + cur2.data
	 




mylist1 = linked_list()
mylist2 = linked_list()

mylist1.append(1)
mylist1.append(2)
mylist1.append(3)
mylist1.append(4)

mylist2.append(5)
mylist2.append(6)
mylist2.append(7)
mylist2.append(8)

addNumbers(mylist1,mylist2)
mylist1.display()


