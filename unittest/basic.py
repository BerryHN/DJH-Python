#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:basic
   Author:jason
   date:2018/3/23
-------------------------------------------------
   Change Activity:2018/3/23:
-------------------------------------------------
"""
import unittest

class TestStringMethods(unittest.TestCase):
	
    def setUp(self):
        print("setup....")
	
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
	    print("teardown...")
	    
if __name__ == '__main__':
    unittest.main()