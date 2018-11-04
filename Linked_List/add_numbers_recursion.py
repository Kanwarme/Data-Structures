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

elems = []
def addNumbers(cur1,cur2):
	sum = cur1.data + cur2.data
	#if last node
	if cur1.next == None:
		last_digit = sum%10
		elems.append(last_digit)
		if(sum>10):
			#carry
			return 1
		return 0

	#if not the last node
	if cur1.next !=None:
		value = sum + addNumbers(cur1.next,cur2.next)
		last_digit = value%10
		elems.append(last_digit)
		if(value>=10):
			#carry
			return 1
		return 0


mylist1 = linked_list()
mylist2 = linked_list()

mylist1.append(5)
mylist1.append(6)
mylist1.append(3)
mylist1.append(6)

mylist2.append(8)
mylist2.append(4)
mylist2.append(2)
mylist2.append(9)
cur1 = mylist1.head
cur2 = mylist2.head
value = addNumbers(cur1.next,cur2.next)
if value == 1:
	elems.append(value)
print(elems[::-1])



