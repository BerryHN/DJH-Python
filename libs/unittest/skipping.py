#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:skipping
   Author:jason
   date:2018/3/23
-------------------------------------------------
   Change Activity:2018/3/23:
-------------------------------------------------
"""
import unittest
import sys


class MyTestCase(unittest.TestCase):
	
	@unittest.skip("demonstrating skipping")
	def test_nothing(self):
		self.fail("shouldn't happen")
	
	@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
	def test_windows_support(self):
		# windows specific testing code
		pass


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
	def test_not_run(self):
		pass


class ExpectedFailureTestCase(unittest.TestCase):
	@unittest.expectedFailure
	def test_fail(self):
		self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
	unittest.main()
