# coding:utf-8

from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
	# 记录优先级
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	# 操作符栈
	opStack = Stack()
	# 后缀
	postfixList = []
	# 单词列表
	tokenList = infixexpr.split(' ')
	for token in tokenList:

		if token.isdigit():  # 分词部分纯数字
			postfixList.append(token)

		elif token == '(':
			opStack.push(token)

		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()

		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	return "".join(postfixList)


def infixToPrefix(infixexpr):
	# 记录优先级
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	# 操作符栈
	opStack = Stack()
	# 后缀
	prefixList = []
	# 单词列表
	tokenList = infixexpr.split(' ')
	for token in tokenList:

		if token.isdigit():
			prefixList.insert(0, token)

		elif token == '(':
			opStack.push(token)

		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				prefixList.insert(0, topToken)
				topToken = opStack.pop()

		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				prefixList.insert(0, opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		prefixList.insert(0, opStack.pop())

	return "".join(prefixList)


def caculatePostfix(postfixexp):
	numbers = "0123456789"
	tokenList = postfixexp.split(' ')
	numStack = Stack()
	for token in tokenList:
		if token in numbers:
			numStack.push(int(token))
		else:
			numb = numStack.pop()
			numa = numStack.pop()
			result = doMath(numa, numb, token)
			numStack.push(result)
	return numStack.pop()


def doMath(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	elif op == '/':
		return a / b


if __name__ == '__main__':
	postList = infixToPostfix("1 + 3 * 5 / ( 6 - 4 )")
	print(postList)

	pretList = infixToPrefix("1 + 3 * 5 / ( 6 - 4 )")
	print(pretList)

	print(caculatePostfix(" ".join(postList)))#对于个位数字运算可以直接加空格，对于多位数字需要在转为后缀字符串时操作
