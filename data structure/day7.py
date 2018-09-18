# coding:utf-8

# 列表嵌套法
def BinaryTree(r):
	return [r, [], []]


def insertLeft(root, newBranch):
	t = []
	if root != []:
		t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def insertRight(root, newBranch):
	t = []
	if root != []:
		t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root


def getRootVal(root):
	return root[0]


def setRootVal(root, newVal):
	root[0] = newVal


def getLeftChild(root):
	return root[1]


def getRightChild(root):
	return root[2]


if __name__ == '__main__':
	r = BinaryTree('a')
	insertLeft(r, 'b')
	insertRight(r, 'c')
	insertRight(getLeftChild(r), 'd')
	insertLeft(getRightChild(getRightChild(r)), 'e')
	print(r)
