# coding:utf-8

import csv


def testReader(file):
	with open(file, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			print(', '.join(row))


def testWriter(file):
	with open(file, 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
		spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def copycsv(source, target):
	csvtarget = open(target, 'w+')
	with open(source, 'r') as csvscource:
		reader = csv.reader(csvscource, delimiter=',')
		for line in reader:
			writer = csv.writer(csvtarget, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(line)
	csvtarget.close()


def testDictReader(file):
	# 院系,专业,年级,学生类别,班级,学号,姓名,学分成绩,更新时间,班级排名,参与班级排名总人数
	with open(file, 'rb') as csvfile:
		dictreader = csv.DictReader(csvfile)
		for row in dictreader:
			print(' '.join([row['院系'], row['专业'], row['学号'], row['姓名']]))


def testDictWriter(file):
	with open(file, 'w') as csvfile:
		fieldnames = ['院系', '专业', '年级', '学生类别', '班级', '学号']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow(
			{'院系': '信息学院', '专业': '计算机科学与技术', '年级': '2011级', '学生类别': '本科(本科)4年', '班级': '计算机11', '学号': '201101245'})
		writer.writerow(
			{'院系': '信息学院', '专业': '计算机科学与技术', '年级': '2011级', '学生类别': '本科(本科)4年', '班级': '计算机11', '学号': '201101275'})


def testpandas_csv():
	import pandas as pd

	obj = pd.read_csv('test.csv')
	print obj
	print type(obj)
	print obj.dtypes


def testnumpy_csv():
	import numpy

	my_matrix = numpy.loadtxt(open("num.csv", "rb"), delimiter=",", skiprows=0)
	print(my_matrix)


if __name__ == '__main__':
	# csvFile = 'test.csv'
	# testReader(csvFile)

	# csvFile = 'test2.csv'
	# testWriter(csvFile)

	# copycsv('test.csv', 'testcopy.csv')

	# testDictReader('test.csv')

	# testDictWriter('test2.csv')
	testnumpy_csv()

# testpandas_csv()
