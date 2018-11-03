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

def compare(mylist1,mylist2):
	if mylist1.length()!= mylist2.length():
		return 0
	else:
		cur1 = mylist1.head
		cur2 = mylist2.head
		while True and cur1.next!= None:
			cur1 = cur1.next
			cur2 = cur2.next
			if(cur1.data!=cur2.data):
				return 0

		return 1	



mylist1 = linked_list()
mylist2 = linked_list()

mylist1.append('R')
mylist1.append('I')
mylist1.append('S')
mylist1.append('H')

mylist2.append('R')
mylist2.append('I')
mylist2.append('S')
mylist2.append('H')

result = compare(mylist1,mylist2)
if result == 1:
	print('Strings are equal')
else:
	print('Strings are not equal')




