# coding:utf-8

def seq_search(lst, key):
	found = False
	pos = 0
	while pos < len(lst) and not found:
		if lst[pos] == key:
			found = True
		else:
			pos = pos + 1
	return found


def ordered_seq_search(lst, key):
	if len(lst) == 0:
		return -1
	mid = len(lst) // 2
	if lst[mid] == key:
		return mid
	else:
		if key < lst[mid]:
			return ordered_seq_search(lst[:mid], key)
		else:
			return ordered_seq_search(lst[mid + 1:], key)


def hashlibTest():
	import hashlib
	str = "Hello,World"
	print(hashlib.md5(str).hexdigest())
	print(hashlib.sha1(str).hexdigest())
	print(hashlib.sha224(str).hexdigest())
	print(hashlib.sha256(str).hexdigest())
	print(hashlib.sha512(str).hexdigest())


def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(len(lst) - 1, i, -1):
			if lst[j] < lst[j - 1]:
				lst[j], lst[j - 1] = lst[j - 1], lst[j]


def selectSort(lst):
	'''
	从后向前，从待排序部分选择，每一趟外层选择，确定最大元素位置，进行一次交换
	:param lst:
	:return:
	'''
	for fillslot in range(len(lst) - 1, 0, -1):
		positionOfMax = 0
		for location in range(1, fillslot + 1):
			if lst[location] > lst[fillslot]:
				positionOfMax = location
		lst[positionOfMax], lst[fillslot] = lst[fillslot], lst[positionOfMax]


def insertSort(lst):
	for i in range(1, len(lst)):
		currentValue = lst[i]
		position = i
		while position > 0 and currentValue < lst[position - 1]:
			lst[position] = lst[position - 1]
			position = position - 1
		lst[position] = currentValue


def mergeSort(lst):
	if len(lst) > 1:
		mid = len(lst) // 2
		lefthalf = lst[:mid]
		righthalf = lst[mid:]

		# 递归
		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = j = k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				lst[k] = lefthalf[i]
				i = i + 1
			else:
				lst[k] = righthalf[j]
				j = j + 1
			k = k + 1
		while i < len(lefthalf):
			lst[k] = lefthalf[i]
			i = i + 1
			k = k + 1
		while j < len(righthalf):
			lst[k] = righthalf[j]
			j = j + 1
			k = k + 1


def quickSort(lst, left, right):
	if left < right:
		i = left
		j = right
		k = lst[i]
		while i < j:
			while i < j and lst[j] > k:
				j = j - 1
			lst[i] = lst[j]
			while i < j and lst[i] < k:
				i = i + 1
			lst[j] = lst[i]
		lst[i] = k
		quickSort(lst, left, i - 1)
		quickSort(lst, i + 1, right)


if __name__ == '__main__':
	seq = [x for x in range(1, 11)]
	# print(seq_search(seq, 8))
	# print(seq_search(seq, 18))
	# print(ordered_seq_search(seq, 8))
	# print(ordered_seq_search(seq, 18))


	# hashlibTest()

	lst = [2, 0, 3, 6, 1, 4, 9, 7, 5, 8]
	quickSort(lst, 0, len(lst) - 1)
	print(lst)
