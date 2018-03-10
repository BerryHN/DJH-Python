# coding:utf-8

# from pythonds.basic.stack import Stack

class Stack(object):
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class Stack2(object):
	'''
	讲index=0 作为栈顶
	'''

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


def test_stack():
	# 测试Stack
	stack = Stack()
	print(stack.is_empty())
	for x in range(1, 11):
		stack.push(x)
	print(stack.size())
	print(stack.is_empty())
	print(stack.peek())
	print(stack.pop())
	print(stack.size())


def check(s):
	lefts = ['(', '[', '{']
	rights = [')', ']', '}']
	stack = Stack()
	for c in s:
		if c in lefts:
			stack.push(c)
	else:
		if stack.is_empty():
			return False
	c_pop = stack.pop()
	if lefts.index(c_pop) != rights.index(c):
		return False
	if stack.is_empty:
		return True
	return False


def divideBy2(decNumber):
	reback = Stack()
	while (decNumber > 0):
		reback.push(decNumber % 2)
	decNumber = decNumber // 2
	binstr = ''
	while not reback.is_empty():
		binstr = binstr + str(reback.pop())
	return binstr


def baseConverter(decNumber, base):
	'''
	将十进制数字转成任意进制数字
	'''
	digits = '0123456789ABCDEF'
	reback = Stack()
	while (decNumber > 0):
		reback.push(decNumber % base)
	decNumber = decNumber // base
	basestr = ''
	while not reback.is_empty():
		basestr = basestr + digits[reback.pop()]
	return basestr


if __name__ == "__main__":
	# s=input()

	# print(divideBy2(15))
	# print(divideBy2(16))

	# print(baseConverter(15,2))
	# print(baseConverter(16,2))
	# print(baseConverter(15,8))
	# print(baseConverter(15,16))
	# print(baseConverter(31,16))
	pass
