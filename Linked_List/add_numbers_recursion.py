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
def carry(cur1,cur2):
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
		value = sum + carry(cur1.next,cur2.next)
		last_digit = value%10
		elems.append(last_digit)
		if(value>=10):
			#carry
			return 1
		return 0

def addNumbers(mylist1,mylist2):
	if mylist1.length() == mylist2.length():
		#when sizes are same
		cur1 = mylist1.head
		cur2 = mylist2.head
		cur1 = cur1.next
		cur2 = cur.next
		value = carry(cur1,cur2)
		if value == 1:
			elems.append(value)
		return elems
	else:
		#when sizes are different
		cur1 = mylist1.head
		cur2 = mylist2.head
		diff = abs(mylist1.length() - mylist2.length())
		if mylist1.length()>mylist2.length():
			for i in range(0,diff):
				cur1 = cur1.next
			cur1 = cur1.next
			cur2 = cur2.next
		if mylist2.length()>mylist1.length():
			for i in range(0,diff):
				cur2 = cur2.next
			cur2 = cur2.next
			cur1 = cur1.next
		value = carry(cur1,cur2)
			


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

elems = addNumbers(mylist1,mylist2)
print(elems[::-1])



