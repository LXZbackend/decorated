# -*- coding: UTF-8 -*-
from decorated.base.function import Function
from unittest.case import TestCase

class MethodTest(TestCase):
    def test_single_level(self):
        # set up
        class Foo(object):
            @Function
            def bar(self, a, b=0):
                return a + b
            
        # test
        result = Foo().bar(1, b=2)
        self.assertEquals(3, result)
        
    def test_multi_levels(self):
        # set up
        class Foo(object):
            @Function
            @Function
            def bar(self, a, b=0):
                return a + b
            
        # test
        result = Foo().bar(1, b=2)
        self.assertEquals(3, result)
        
    def test_static_method(self):
        # set up
        class Foo(object):
            @staticmethod
            @Function
            def bar(a, b=0):
                return a + b
            
        # test
        result = Foo.bar(1, b=2)
        self.assertEqual(3, result)
        
    def test_class_method(self):
        # set up
        class Foo(object):
            @classmethod
            @Function
            def bar(cls, a, b=0):
                return a + b
            
        # test
        result = Foo.bar(1, b=2)
        self.assertEqual(3, result)
        
    def test_get_method(self):
        # set up
        class Foo(object):
            @Function
            def bar(self, a, b=0):
                return a + b
            
        # test
        self.assertIsInstance(Foo.bar, Function)
        