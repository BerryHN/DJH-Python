# coding:utf-8

from pythonds.basic.stack import Stack


class StacToQueue(object):
	def __init__(self):
		self.stack_one = Stack()
		self.stack_two = Stack()

	def enqueue(self, item):
		self.stack_one.push(item)

	def dequeue(self):
		if self.stack_two.isEmpty():
			while not self.stack_one.isEmpty():
				self.stack_two.push(self.stack_one.pop())
		return self.stack_two.pop()

	def size(self):
		return len(self.stack_one) + len(self.stack_two)

	def isEmpty(self):
		return self.size() == 0


class Dequeue(object):
	def __init__(self):
		self.items = []

	def enqueueFront(self, item):
		self.items.insert(0, item)

	def dequeueRear(self):
		return self.items.pop()

	def enqueueRear(self, item):
		self.items.append(item)

	def dequeueFront(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def isEMpty(self):
		return self.items == []


def palchecker(string):
	chardequeue = Dequeue()
	for ch in string:
		chardequeue.enqueueFront(ch)
	while not chardequeue.isEMpty():
		front = chardequeue.dequeueFront()
		rear = chardequeue.dequeueRear()
		if front != rear:
			return False
	return True


if __name__ == '__main__':
	queue = StacToQueue()
	for x in range(5):
		queue.enqueue(x)
	for x in range(5):
		print(queue.dequeue())

	print("回文判断：")
	print(palchecker("123321"))
	print(palchecker("124561"))
