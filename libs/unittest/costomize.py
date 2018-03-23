#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:costomize
   Author:jason
   date:2018/3/23
-------------------------------------------------
   Change Activity:2018/3/23:
-------------------------------------------------
"""
import unittest
from tkinter import Widget


class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget('The widget')
	
	def tearDown(self):
		self.widget.dispose()


def suite():
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase('test_default_widget_size'))
	suite.addTest(WidgetTestCase('test_widget_resize'))
	return suite


if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())
