from sys import maxsize

def createStack():
	stack = []
	return stack

def isEmpty(stack):
	return len(stack) == 0

def push(mainStack, auxStack, item):
	if(isEmpty(mainStack) == True and isEmpty(auxStack)==True):
		mainStack.append(item)
		auxStack.append(item)
		return
	if(item>auxStack[len(auxStack)-1]):
		auxStack.append(auxStack[len(auxStack)-1])
	else:
		auxStack.append(item)
	mainStack.append(item)

def pop(stack):
	if(isEmpty(stack)):
		return str(-maxsize-1)
	return stack.pop()

def getMin(mainStack, auxStack):
	while(True):
		elem1=pop(mainStack)
		elem2=pop(auxStack)
		if(elem1 == elem2):
			break
	return elem1

mainStack = createStack()
auxStack = createStack()

push(mainStack,auxStack,str(18))
push(mainStack,auxStack,str(19))
push(mainStack,auxStack,str(29))
push(mainStack,auxStack,str(15))
push(mainStack,auxStack,str(16))

# print(pop(auxStack))
# print(pop(auxStack))
# print(pop(auxStack))
# print(pop(auxStack))
# print(pop(auxStack))

# print(pop(mainStack))
# print(pop(mainStack))
# print(pop(mainStack))
# print(pop(mainStack))
# print(pop(mainStack))


print(getMin(mainStack, auxStack))
print(getMin(mainStack, auxStack))

