#!/usr/bin/env python3

import unittest

class CoreStack(unittest.TestCase):
    """core stack functions: direct interations with []Stack.stack"""

    def setUp(self):
        stack.stack = []

    def test_inspect(self):
        """stack viewer"""
        result = stack.inspect()
        self.assertEqual(result, [])
        try:
            assert result == [], "fatal: failed to read the stack: not continuing"
        except AssertionError as error:
            raise RuntimeError(error) from AssertionError

    def test_push(self):
        """put something on the stack"""
        stack.push(9)
        result = stack.inspect()
        self.assertEqual(result, [9])

    def test_pushn(self):
        """put n things on the stack"""
        stack.pushn([i for i in range(100)])
        result = stack.inspect()
        self.assertEqual(result, [i for i in range(100)])

    def test_pop(self):
        """pop from stack"""
        stack.push(9)
        stack.pop()
        result = stack.inspect()
        self.assertEqual(result, [])

    def test_popn(self):
        """pop n things from stack"""
        stack.pushn([i for i in range(1000)])
        result = stack.inspect()
        self.assertEqual(result, [i for i in range(1000)])

    def test_copy(self):
        """copy the top of the stack"""
        stack.push(9)
        result = stack.copy()
        self.assertEqual(result, 9)

    def test_copyn(self):
        """copy n items from the top of the stack and return a tuple"""
        stack.pushn([i for i in range(10)])
        result = stack.copyn(2)
        self.assertEqual(result, tuple(stack.inspect()[:-2]))

    def test_insert(self):
        """insert an item at an index"""
        stack.pushn([i for i in range(10)])
        stack.insert(5, 7)
        self.assertEqual(stack.inspect()[7], 5)

    def test_insertn(self):
        """insert items at index n and up"""
        stack.pushn([i for i in range(10)])
        stack.insertn([2, 3, 4, 5], 2)
        self.assertEqual(stack.inspect()[2:6], [2, 3, 4, 5])

    def test_remove(self):
        """remove an item from an index"""
        stack.pushn([i for i in range(10)])
        stack.remove(5)
        lst = [i for i in range(10)]
        lst.remove(5)
        self.assertEqual(stack.inspect(), lst)

    def test_index(self):
        """return a 1-indexed item from the end of the list"""
        stack.pushn(list(reversed([i for i in range(10)])))
        result = stack.index(7)
        self.assertEqual(result, stack.inspect()[-7])

    def test_clean(self):
        """clear the stack and return the old stack"""
        stack.pushn([i for i in range(10)])
        result = stack.clean()
        self.assertEqual(result, stack.inspect())

class Math(unittest.TestCase):
    """mathematical functions: proxied stack interactions, direct interaction with basic Python math operators"""

    def setUp(self):
        stack.clean()
        stack.pushn([(i, j) for i, j in enumerate(reversed(range(100)))])

    # addition

    def test_add_nums(self):
        """add some numbers"""

    def test_add_strs(self):
        pass

    def test_add_numstr(self):
        pass

    def test_add_failure(self):
        pass

    # subtraction

    def test_sub_nums(self):
        pass

    def test_sub_strs(self):
        pass

    def test_sub_numstr(self):
        pass

    def test_sub_failure(self):
        pass

    # multilpication

    def test_mlt_nums(self):
        pass

    def test_mlt_strs(self):
        pass

    def test_mlt_numstr(self):
        pass

    def test_mlt_failure(self):
        pass

    # divmod

    def test_dmd_nums(self):
        pass

'''
class StackOps(unittest.TestCase):
    """stack operators: proxied []Stack.stack interaction through CoreStack"""
    pass

class Types(unittest.TestCase):
    """interactions between certain types and operators, and type-specific functions"""
    pass

class MathConst(unittest.TestCase):
    """tests of number-special functions (Python's Math library) and builtin constants"""
    pass

class Parsing(unittest.TestCase):
    """tests specific to syntax and the parser, but not the runner"""
    pass

class Runtime(unittest.TestCase):
    """variables, memory, function defs/calls, language features: reliant on all o the previous classes"""
    pass

class FailMe(unittest.TestCase):
    """things that should explicitly fail: zero division, for instance"""
    pass
'''

if __name__ == '__main__':
    import mouse15

    stack = mouse15.Stack()

    mouse = mouse15.Mouse()

    unittest.main()
