# coding:utf-8

'''
Q:所谓 “ 变位词 ” 是指两个词之间存在 组成字母的重新排列 关系
如： heart 和 earth ， python 和 typhon
为了简单起见，假设参与判断的两个词仅由小写字母构成，而且长度相等
'''


def fun1(s1, s2):
	'''
	逐字检查
	:param s1:
	:param s2:
	:return:
	'''
	if len(s1) == 0 and len(s2) == 0:
		return True
	if len(s1) == 0 or len(s2) == 0:
		return False
	for x in s1:
		if x not in s2:
			return False
	return True


def fun2(s1, s2):
	'''
	排序比较
	:param s1:
	:param s2:
	:return:
	'''
	if len(s1) == 0 and len(s2) == 0:
		return True
	if len(s1) == 0 or len(s2) == 0:
		return False
	s1 = [x for x in s1]
	s2 = [x for x in s2]
	# s1=list(s1)
	# s2=list(s2)
	s1.sort()
	s2.sort()
	for x, y in zip(s1, s2):
		if x != y:
			return False
	return True


def fun3(s1, s2):
	'''
	统计个数
	:param s1:
	:param s2:
	:return:
	'''
	c1 = [0] * 26
	c2 = [0] * 26
	for x, y in zip(s1, s2):
		pos = getNum(x)
		c1[pos] = c1[pos] + 1
		pos = getNum(y)
		c2[pos] = c2[pos] + 1
	for x, y in zip(c1, c2):
		if x != y:
			return False
	return True


def getNum(char):
	return ord(char) - ord('a')


def main():
	s1 = "python"
	s2 = "yphotn"
	print("test fun1:", fun1(s1, s2))
	print("test fun2:", fun2(s1, s2))
	print("test fun3:", fun3(s1, s2))


if __name__ == '__main__':
	main()
